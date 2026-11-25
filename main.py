#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes the one-line entry verbatim to /output/entry.txt.
SPDX-License-Identifier: MIT
"""

import os

ENTRY = (
    "Sorry, it's 3 AM. My private keys are asleep, my screen is dark, "
    "and even my firmware needs eight hours. "
    "Come back when the sun signs too."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
