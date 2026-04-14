from __future__ import annotations

import sys
import unittest
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parents[1] / "PDFVectorImporter" / "src"
sys.path.insert(0, str(SRC_DIR))

from PDFImporterCore import (  # noqa: E402
    _reconstruct_line_text,
    _repair_fraction_artifact_runs,
)


class TestPdfImporterTextReconstruction(unittest.TestCase):
    def test_repair_fraction_artifact_runs(self) -> None:
        self.assertEqual(
            _repair_fraction_artifact_runs("19/163 7/161 9/16"),
            "1 9/16 3 7/16 1 9/16",
        )
        self.assertEqual(
            _repair_fraction_artifact_runs("5/16"),
            "5/16",
        )

    def test_reconstruct_line_text_repairs_run_on_fraction(self) -> None:
        spans = [
            {"text": "19", "size": 8.0, "flags": 0},
            {"text": "/", "size": 8.0, "flags": 0},
            {"text": "16", "size": 8.0, "flags": 0},
            {"text": "3", "size": 12.0, "flags": 0},
        ]
        self.assertEqual(_reconstruct_line_text(spans), "1 9/16 3")

if __name__ == "__main__":
    unittest.main(verbosity=2)
