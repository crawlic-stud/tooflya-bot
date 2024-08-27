from pathlib import Path
from django.shortcuts import render
from PIL import Image

images = [
    "/static/images/sneaker1.jpg",
    "/static/images/sneaker2.jpg",
    "/static/images/sneaker3.jpg",
]


def compress_images():
    for image in Path("src/app/static/images").glob("*.jpg"):
        pil_image = Image.open(image)
        pil_image.save(image, format="jpeg", quality=20)


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
            * 10
        },
    )
