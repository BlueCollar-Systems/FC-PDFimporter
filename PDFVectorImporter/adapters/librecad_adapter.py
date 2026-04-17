#!/usr/bin/env python3
"""
LibreCAD adapter for PDF Vector Importer QA.

Runs the standalone LibreCAD PDF importer CLI (PDF -> DXF pipeline) and
classifies the run as PASS/FAIL/BLOCKED for the central QA workbook runner.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Optional


def load_json(path: Optional[str]) -> dict:
    if not path:
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_path(value: Optional[str], base_dir: Optional[str] = None) -> Optional[str]:
    if value is None:
        return None
    raw = os.path.expandvars(str(value))
    # Allow command-style executables like "python" without forcing path resolution.
    if ("/" not in raw and "\\" not in raw and not Path(raw).is_absolute()):
        return raw
    p = Path(raw).expanduser()
    if not p.is_absolute() and base_dir:
        p = Path(base_dir) / p
    return str(p.resolve())


def run_librecad_cli(
    python_exe: str,
    repo_dir: str,
    input_pdf: str,
    output_dxf: str,
    mode: str,
    page_range: str,
    summary_json: str,
    timeout_seconds: int,
    no_text: bool = False,
    no_images: bool = False,
    no_arcs: bool = False,
) -> subprocess.CompletedProcess:
    cmd = [
        python_exe,
        "-m",
        "librecad_pdf_importer.cli",
        input_pdf,
        "--out",
        output_dxf,
        "--mode",
        mode,
        "--pages",
        page_range,
        "--json",
        summary_json,
    ]
    if no_text:
        cmd.append("--no-text")
    if no_images:
        cmd.append("--no-images")
    if no_arcs:
        cmd.append("--no-arcs")

    return subprocess.run(
        cmd,
        cwd=repo_dir,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
        check=False,
    )


def classify_result(summary: dict, min_entities: int, max_seconds: int, runtime_seconds: float) -> tuple[str, str]:
    export = summary.get("export", {})
    entity_count = int(export.get("entity_count", 0))
    output_path = export.get("output_path")
    if not output_path:
        return "FAIL", "Exporter did not report an output path."
    if entity_count < min_entities:
        return "FAIL", f"Entity count {entity_count} below required minimum {min_entities}."
    if max_seconds > 0 and runtime_seconds > max_seconds:
        return "FAIL", f"Runtime {runtime_seconds:.2f}s exceeded cap {max_seconds}s."
    return "PASS", f"Exported {entity_count} entities."


def main() -> int:
    parser = argparse.ArgumentParser(description="LibreCAD adapter for PDF importer QA.")
    parser.add_argument("--config", help="Path to qa_config.json", required=False)
    parser.add_argument("--test-id", required=True)
    parser.add_argument("--input", required=True, help="Input PDF path")
    parser.add_argument("--mode", default="auto",
                        choices=["auto", "vector", "raster", "hybrid"])
    parser.add_argument("--page-range", default="1")
    parser.add_argument("--min-entities", type=int, default=1)
    parser.add_argument("--runtime-cap-seconds", type=int, default=0)
    parser.add_argument("--no-text", action="store_true")
    parser.add_argument("--no-images", action="store_true")
    parser.add_argument("--no-arcs", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cfg = load_json(args.config)
    config_dir = str(Path(args.config).expanduser().resolve().parent) if args.config else os.getcwd()
    librecad_cfg = cfg.get("librecad", {})

    repo_dir = normalize_path(librecad_cfg.get("repo_dir"), config_dir)
    python_exe = normalize_path(librecad_cfg.get("python_exe"), config_dir) or sys.executable
    input_pdf = normalize_path(args.input, config_dir)
    timeout_seconds = int(librecad_cfg.get("timeout_seconds", 1800))

    if args.dry_run:
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "LC",
                    "status": "DRY_RUN",
                    "message": "LibreCAD adapter config parsed successfully.",
                    "repo_dir": repo_dir,
                    "python_exe": python_exe,
                },
                indent=2,
            )
        )
        return 0

    if not repo_dir or not os.path.isdir(repo_dir):
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "LC",
                    "status": "ERROR",
                    "message": f"LibreCAD repo_dir not found: {repo_dir}",
                },
                indent=2,
            )
        )
        return 2
    if not input_pdf or not os.path.isfile(input_pdf):
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "LC",
                    "status": "ERROR",
                    "message": f"Input PDF not found: {input_pdf}",
                },
                indent=2,
            )
        )
        return 2

    with tempfile.TemporaryDirectory(prefix="bc_pdf_lc_qa_") as td:
        summary_path = os.path.join(td, f"{args.test_id}_lc_summary.json")
        output_dxf = os.path.join(td, f"{args.test_id}.dxf")

        started = time.perf_counter()
        try:
            proc = run_librecad_cli(
                python_exe=python_exe,
                repo_dir=repo_dir,
                input_pdf=input_pdf,
                output_dxf=output_dxf,
                mode=args.mode,
                page_range=args.page_range,
                summary_json=summary_path,
                timeout_seconds=timeout_seconds,
                no_text=args.no_text,
                no_images=args.no_images,
                no_arcs=args.no_arcs,
            )
        except subprocess.TimeoutExpired:
            print(
                json.dumps(
                    {
                        "test_id": args.test_id,
                        "platform": "LC",
                        "status": "FAIL",
                        "message": f"Timed out after {timeout_seconds}s.",
                    },
                    indent=2,
                )
            )
            return 1

        runtime_seconds = round(time.perf_counter() - started, 3)
        if proc.returncode != 0:
            print(
                json.dumps(
                    {
                        "test_id": args.test_id,
                        "platform": "LC",
                        "status": "FAIL",
                        "message": f"CLI exited {proc.returncode}",
                        "stdout": (proc.stdout or "")[-2000:],
                        "stderr": (proc.stderr or "")[-2000:],
                    },
                    indent=2,
                )
            )
            return proc.returncode

        if not os.path.isfile(summary_path):
            print(
                json.dumps(
                    {
                        "test_id": args.test_id,
                        "platform": "LC",
                        "status": "FAIL",
                        "message": "CLI did not produce summary JSON.",
                        "stdout": (proc.stdout or "")[-2000:],
                        "stderr": (proc.stderr or "")[-2000:],
                    },
                    indent=2,
                )
            )
            return 1

        with open(summary_path, "r", encoding="utf-8") as f:
            summary = json.load(f)

        status, message = classify_result(summary, args.min_entities, args.runtime_cap_seconds, runtime_seconds)
        print(
            json.dumps(
                {
                    "test_id": args.test_id,
                    "platform": "LC",
                    "status": status,
                    "message": message,
                    "runtime_seconds": runtime_seconds,
                    "summary": summary,
                },
                indent=2,
            )
        )
        return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
