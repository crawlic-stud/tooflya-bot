import io
from pathlib import Path

from PIL import Image


IMAGES_URL = "images/"
IMAGES_ROOT = "static/images/"

STATIC_IMAGES_PATH = Path(IMAGES_ROOT)
STATIC_IMAGES_PATH.mkdir(exist_ok=True, parents=True)

_IMAGE_SIZE = [512.0, 512.0]
_IMAGE_QUALITY = 85


def optimize_and_save_image(image_bytes: io.BytesIO, filename: str):
    pil_image = Image.open(image_bytes)
    pil_image.thumbnail(_IMAGE_SIZE, Image.Resampling.LANCZOS)
    new_filename = f'{filename.split(".")[0]}.webp'
    optimized_image_path = STATIC_IMAGES_PATH / new_filename
    pil_image.save(optimized_image_path, format="webp", optimize=True, quality=_IMAGE_QUALITY)
    return IMAGES_URL + new_filename
