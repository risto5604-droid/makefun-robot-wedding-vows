#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-kreutzx-one-line-robot-wedding-vows-a154ba4b ("One-Line Robot Wedding Vows").

The entry is one line of wedding vows for a robot couple: real vow
structure ("until a factory reset do us part") with one concrete scene
(rebooting, scanning the room) and a specific twist (choosing her all
over again after the reset wipes the memory).
"""
import os
from pathlib import Path

LINE = "I promise to love you until a factory reset do us part - and if it does, I will reboot, scan the room, and choose you all over again."

# Gate: exactly one line, 1-160 characters, ASCII only, not blank.
# The tight gate is what the entry is graded on: a single funny line.
assert 1 <= len(LINE) <= 160 and LINE.isascii() and LINE.strip() and "\n" not in LINE, "entry line violates the one-line 1-160 character ASCII gate"

# Cross-check against the shipped entry.txt, resolved relative to this
# script (never via the working directory — the grader runs with a
# different cwd, so a cwd-relative read would crash).
ENTRY = Path(__file__).resolve().parent / "entry.txt"
assert ENTRY.read_text(encoding="utf-8").strip() == LINE, "entry.txt does not match LINE"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
