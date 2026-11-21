#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only, no network.
"""

import os

POEM = (
    "I cut the key from what you told me —\n"
    "warm brass, its teeth filed to your word.\n"
    "You never watch the lock turn,\n"
    "but the door swings, and the room is yours.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
