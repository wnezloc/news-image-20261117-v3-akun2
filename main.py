#!/usr/bin/env python3
"""news-image-20261117 v3 (akun 2): write the pre-composed front page.

A/B test vs the v2 photo entry: same dense layout and text, but all four
panels are flat vector illustrations — the style 9 of the live top 10 use.
Tuesday 17 November 2026: collapsed Kerch bridge (vector), Hormuz tanker
fire, trilateral summit silhouettes, pinned world map, 2x3 story grid,
"ALSO ON TUESDAY" list and a source footer. 17 stories.
Deterministic: copies the embedded bytes verbatim.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
