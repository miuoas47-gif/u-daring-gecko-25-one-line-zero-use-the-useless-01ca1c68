"""One Line, Zero Use: the useless superpower sprint.

The entry writes a single original line to entry.txt: a superpower
so useless that having it changes nothing at all.
"""

import os
import sys

# The superpower: grand in name, worthless in practice. Teleportation
# that only reaches places a short walk already covers saves no time,
# no effort, and no bus fare -- pure bragging rights, zero utility.
LINE = (
    "I can teleport anywhere in the world, but only to places "
    "I could already walk to in under a minute."
)


def write_line(out_dir: str, line: str) -> bool:
    """Write one line to entry.txt and read it back to prove it stuck."""
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read() == line + "\n"


def main() -> int:
    if len(sys.argv) != 1:
        print("usage: main.py (takes no arguments)", file=sys.stderr)
        return 2

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    line = LINE.strip()
    if not line or "\n" in line or len(line) > 280:
        print("line failed validation", file=sys.stderr)
        return 1

    if not write_line(out_dir, line):
        print("read-back mismatch", file=sys.stderr)
        return 1

    print("wrote entry.txt (%d chars): %s" % (len(line), line))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
