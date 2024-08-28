from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.objects.all()

    items = [
        {
            "name": product.name,
            "images": [image.image.url for image in product.images.all()]
        }
        for product in products
    ]

    return render(
        request,
        "catalog.html",
        context={"items": items},
    )
