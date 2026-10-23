#!/usr/bin/env python3
"""Flag dead (flat) frames in a rendered MP4.

A "dead frame" is a stretch where the picture carries no information: one solid
colour with nothing on it. They appear when a scene transition empties the frame
before the next beat arrives, and they read as a hiccup in an otherwise authored
film. They are almost invisible in a contact sheet, because a contact sheet is
mostly empty space anyway.

Usage:
    python3 deadframe.py renders/out.mp4 [--min 0.2] [--std 6] [--width 256]

Exit code 1 when dead stretches are found, so it can gate a render.
"""
import argparse
import json
import subprocess
import sys


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height,r_frame_rate",
         "-of", "json", path],
        capture_output=True, text=True, check=True).stdout
    s = json.loads(out)["streams"][0]
    num, den = s["r_frame_rate"].split("/")
    return s["width"], s["height"], float(num) / float(den)


def frames(path, width):
    w, h, fps = probe(path)
    height = max(2, round(h * width / w / 2) * 2)
    proc = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path,
         "-vf", f"scale={width}:{height},format=gray",
         "-f", "rawvideo", "-"],
        capture_output=True, check=True)
    size = width * height
    data = proc.stdout
    return [data[i:i + size] for i in range(0, len(data) - size + 1, size)], fps


def stddev(buf):
    # 16-bin histogram is enough to tell flat from designed, and it is fast
    hist = [0] * 16
    for b in buf:
        hist[b >> 4] += 1
    n = len(buf)
    mean = sum(i * c for i, c in enumerate(hist)) / n
    var = sum(c * (i - mean) ** 2 for i, c in enumerate(hist)) / n
    return var ** 0.5 * 16


def runs(flags, fps, min_frames):
    out, start = [], None
    for i, flat in enumerate(flags):
        if flat and start is None:
            start = i
        elif not flat and start is not None:
            if i - start >= min_frames:
                out.append((start / fps, i / fps))
            start = None
    if start is not None and len(flags) - start >= min_frames:
        out.append((start / fps, len(flags) / fps))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--min", type=float, default=0.2, help="minimum dead stretch, seconds")
    ap.add_argument("--std", type=float, default=6.0, help="flatness threshold (0-255 std dev)")
    ap.add_argument("--width", type=int, default=256)
    a = ap.parse_args()

    bufs, fps = frames(a.video, a.width)
    flags = [stddev(b) < a.std for b in bufs]
    bad = runs(flags, fps, max(1, round(a.min * fps)))

    total = len(bufs) / fps
    print(f"{a.video}: {total:.2f}s, {len(bufs)} frames @ {fps:.0f} fps")
    if not bad:
        print("  ok — no dead frames")
        return 0
    for s, e in bad:
        print(f"  dead frame {s:.2f}s → {e:.2f}s  ({e - s:.2f}s)")
    print(f"  {len(bad)} dead stretch(es); fill them or cut them out")
    return 1


if __name__ == "__main__":
    sys.exit(main())
