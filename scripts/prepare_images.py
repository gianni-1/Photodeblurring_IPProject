"""Prepare raw landscape images as consistently sized RGB PNG files."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


SUPPORTED_SUFFIXES = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp"}


def prepare_image(input_path: Path, output_path: Path, size: int) -> None:
    """Center-crop an image to a square and resize it without distortion."""
    with Image.open(input_path) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
        width, height = image.size
        crop_size = min(width, height)
        left = (width - crop_size) // 2
        top = (height - crop_size) // 2
        square = image.crop((left, top, left + crop_size, top + crop_size))
        prepared = square.resize((size, size), Image.Resampling.LANCZOS)
        prepared.save(output_path, format="PNG", optimize=True)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Center-crop raw images and save consistent RGB PNG files."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("data/raw"),
        help="Directory containing the original images.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/processed/clean"),
        help="Directory for prepared PNG images.",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=512,
        help="Square output width and height in pixels.",
    )
    return parser.parse_args()


def main() -> None:
    """Prepare every supported image in the input directory."""
    args = parse_args()
    if args.size <= 0:
        raise ValueError("--size must be a positive integer.")

    input_paths = sorted(
        path
        for path in args.input_dir.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES
    )
    if not input_paths:
        raise FileNotFoundError(f"No supported images found in {args.input_dir}.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for input_path in input_paths:
        output_path = args.output_dir / f"{input_path.stem}.png"
        prepare_image(input_path, output_path, args.size)
        print(f"Prepared {input_path} -> {output_path} ({args.size}x{args.size}, RGB PNG)")


if __name__ == "__main__":
    main()
