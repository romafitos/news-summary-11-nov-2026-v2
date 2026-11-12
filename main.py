"""news-summary-01 entry, v2 (Python 3.13, stdlib only).

Writes the summary in summary.txt beside this file to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The summary itself is authored in summary.txt; this file only
copies it verbatim, never edits it.
Deterministic: the output is a byte copy of the file, so two runs
always write the same bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SRC = HERE / "summary.txt"
OUT.mkdir(parents=True, exist_ok=True)
if SRC.stat().st_size == 0:
    raise SystemExit("summary.txt is empty")
dest = OUT / "entry.txt"
shutil.copyfile(SRC, dest)
if dest.stat().st_size != SRC.stat().st_size:
    raise SystemExit("entry copy size mismatch")
