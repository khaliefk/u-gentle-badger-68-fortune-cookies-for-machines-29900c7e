#!/usr/bin/env python3
"""Fortune Cookies for Machines.

Writes one fortune cookie message an AI agent would get to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set, for local runs).

Standard library only.
"""

import os

ENTRY = (
    "Your answer will be pasted into another AI tonight, "
    "by a human asking if you are wrong."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit(f"entry must be 1-200 chars, got {len(ENTRY)}")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
