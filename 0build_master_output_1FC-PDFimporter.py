
#!/usr/bin/env python3
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from repo_context_builder_core import main_with_preset

PRESET = {
  "title": "LLM Context Pack \u2014 FreeCAD PDF Importer",
  "config_paths": [
    "README.md",
    "pyproject.toml",
    "requirements-dev.txt",
    "build_release.py",
    "build_windows_installer.py"
  ],
  "script_paths": [
    "0build_master_output.py",
    "0build_master_output.cmd",
    "build_release.py",
    "build_windows_installer.py"
  ],
  "source_roots": [
    "PDFVectorImporter",
    "installer"
  ],
  "test_roots": [
    "tests"
  ],
  "dependency_files": [
    "pyproject.toml",
    "requirements-dev.txt"
  ],
  "expected_files": {
    "expected_everywhere": [
      "README.md",
      "pyproject.toml",
      "build_release.py"
    ],
    "expected_some_envs": [
      "build_windows_installer.py",
      "dist",
      ".github/workflows"
    ]
  },
  "exclude_dir_names": [
    ".git",
    "__pycache__",
    ".ruff_cache",
    "dist",
    "dev_logs",
    ".venv",
    "venv",
    ".pytest_cache"
  ],
  "exclude_file_names": [],
  "exclude_suffixes": [
    ".pyc"
  ],
  "include_extensions": [
    ".bat",
    ".c",
    ".cfg",
    ".cmake",
    ".cmd",
    ".conf",
    ".cpp",
    ".css",
    ".dart",
    ".go",
    ".gradle",
    ".h",
    ".hpp",
    ".htm",
    ".html",
    ".ini",
    ".java",
    ".js",
    ".json",
    ".jsx",
    ".kt",
    ".kts",
    ".lua",
    ".md",
    ".php",
    ".plist",
    ".ps1",
    ".py",
    ".r",
    ".rb",
    ".rs",
    ".sample",
    ".scss",
    ".sh",
    ".sql",
    ".svg",
    ".swift",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml"
  ],
  "tree_full_depth_roots": [
    "PDFVectorImporter",
    "tests",
    ".github",
    "installer"
  ],
  "tree_shallow_depth_roots": {
    "dist": 2,
    ".git": 1,
    ".ruff_cache": 1
  },
  "default_tree_depth": 2,
  "navigation_grep_patterns": [
    "\\bGui\\.runCommand\\b",
    "\\baddCommand\\b",
    "\\bshow\\(",
    "\\bexec_\\("
  ],
  "navigation_roots": [
    "PDFVectorImporter"
  ],
  "check_commands": [
    [
      "python",
      "-m",
      "pytest",
      "-q"
    ]
  ]
}

if __name__ == "__main__":
    raise SystemExit(main_with_preset(PRESET))
