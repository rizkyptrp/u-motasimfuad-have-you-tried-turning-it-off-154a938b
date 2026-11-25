#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line a hopeless tech support agent says to a desperate
customer to /output/entry.txt. Stdlib only, deterministic, no network,
no model calls.
"""

import os

LINE = (
    "I can hear how urgent this is, so I'm putting you on a brief hold "
    "while I Google your exact error message."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
