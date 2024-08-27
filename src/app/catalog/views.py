from pathlib import Path
import random
from django.shortcuts import render
from PIL import Image

images = [
    "/static/images/optimized/sneaker1.webp",
    "/static/images/optimized/sneaker2.webp",
    "/static/images/optimized/sneaker3.webp",
    "/static/images/optimized/dimas.webp",
]

optimized_folder = Path("./static/images/optimized")
optimized_folder.mkdir(exist_ok=True)

def compress_images():
    for image_path in optimized_folder.parent.glob("*.jpg"):
        pil_image = Image.open(image_path)
        pil_image.thumbnail([512.0, 512.0], Image.Resampling.LANCZOS)
        optimized_image_path = (
            optimized_folder / f'{image_path.name.removesuffix(".jpg")}.webp'
        )
        pil_image.save(optimized_image_path, format="webp", optimize=True, quality=85)


compress_images()


# Create your views here.
def index(request):
    return render(
        request,
        "catalog.html",
        context={
            "items": [
                {"name": "Туфля 3000", "images": images},
                {"name": "Туфля GEL-KAYANO 28", "images": images},
                {"name": "Туфля GEL-NIMBUS 24", "images": images},
                {"name": "Туфля GEL-CUMULUS 24", "images": images},
                {"name": "Туфля GEL-CONTEND 7", "images": images},
                {"name": "Туфля GEL-EXCITE 9", "images": images},
            ]
        },
    )
