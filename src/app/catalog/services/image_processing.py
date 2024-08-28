import io
from pathlib import Path

from PIL import Image

STATIC_IMAGES_PATH = "static/images/"
IMAGES_FOLDER = Path("src/app") / STATIC_IMAGES_PATH
IMAGES_FOLDER.mkdir(exist_ok=True, parents=True)


def optimize_and_save_image(image_bytes: io.BytesIO, filename: str):
    pil_image = Image.open(image_bytes)
    pil_image.thumbnail([512.0, 512.0], Image.Resampling.LANCZOS)
    new_filename = f'{filename.split(".")[0]}.webp'
    optimized_image_path = IMAGES_FOLDER / new_filename
    pil_image.save(optimized_image_path, format="webp", optimize=True, quality=85)
    return STATIC_IMAGES_PATH + new_filename
