#!/usr/bin/env python3
# 3 AM Excuse — the hardware wallet says no to signing at 3 AM.
# Writes the single entry line to /output/entry.txt exactly as-is.
# SPDX-License-Identifier: MIT

from pathlib import Path

TEXT = "Sorry, it's 3 AM. My private keys are asleep, my screen is dark, and even my firmware needs eight hours. Come back when the sun signs too."


def run():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":  # entry point
    run()
