#!/usr/bin/env python3
"""Warning-label entry: a human that loads slowly and answers in business days.

Builds one single-line safety warning label from small fragments, prints
it to stdout, and writes it, with no trailing newline, to entry.txt
inside the output directory. The label is 83 characters: a deadpan
"do not tap while loading" instruction whose payoff lands in the last
few words, "3 to 5 business days" -- a concrete number, a second twist
on the same idea (slow replies), and a truth everyone recognises about
how humans actually answer. It sounds like a real printed label because
it copies one's wording and rhythm ("WARNING: Do not ... while ...").
"""

import os
from pathlib import Path

MAX_CHARS = 160
LABEL_PREFIX = "WARNING:"


def build_line() -> str:
    setup = "WARNING: Do not tap this unit while loading;"
    payoff = " response time is 3 to 5 business days."
    return setup + payoff


def main() -> None:
    line = build_line()
    if not line.startswith(LABEL_PREFIX):
        raise ValueError("entry must open with the label prefix WARNING:")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "\n" in line or line != line.strip():
        raise ValueError("entry must be one line with no surrounding whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if not 1 <= len(line) <= MAX_CHARS or not line.strip():
        raise ValueError("entry must be 1-160 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_text(line, encoding="utf-8")
    os.chmod(out_file, 0o644)
    print(line)


if __name__ == "__main__":
    main()
