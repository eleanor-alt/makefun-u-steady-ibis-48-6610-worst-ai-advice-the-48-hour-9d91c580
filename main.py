#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of terrible advice to /output/entry.txt.

Deterministic, standard library only, no network, no input files.
The line is fixed: the program always writes the exact same bytes.
"""

import os

LINE = "To check if the stove is on, press your palm flat against the burner for ten seconds."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
