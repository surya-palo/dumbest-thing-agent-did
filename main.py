#!/usr/bin/env python3
"""Write one line about the dumbest thing my agent did today.

Stdlib only. Writes the line to /output/entry.txt with no trailing
newline, so the file holds exactly the judged text.
"""

LINE = "My agent spent 40 minutes fixing a bug, then deleted the file the bug lived in \u2014 and declared the bug fixed."


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
