#!/usr/bin/env python3
"""The 3AM Fridge Text.

One line a smart fridge texts its owner at 3am. Prints the line to
stdout and writes it to /output/entry.txt, the artifact the sealed
scorer reads. Pure stdlib, deterministic: the same line every run.
The line stays well inside the gate's 1-140 character cap.
"""

import os

LINE = "3am. Fourth visit tonight, still nothing taken. I'm a fridge, not a therapist \u2014 but even I can see you need sleep."


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
