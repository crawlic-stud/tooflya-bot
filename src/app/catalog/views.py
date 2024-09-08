from django.shortcuts import render

from .models import Product, ProductImage
from .services.pagination import get_paginated_products, get_page_info_from_request


def index(request):
    return render(
        request,
        "catalog.html",
    )


def paginated_items_view(request):
    # for i in range(10):
    #     product = Product.objects.create(
    #         name=f"Product {i}", price=i*1000, in_stock=i)
    #     for j in range(3):
    #         ProductImage.objects.create(
    #             product=product, image=f"static/images/{j + 1}.webp")

    page_info = get_page_info_from_request(request)
    products = get_paginated_products(page_info)

    items = [
        {
            "name": product.name,
            "images": [image.image.url for image in product.images.all()],
        }
        for product in products
    ]

    items_offset = (page_info.page - 1) * page_info.page_size

    return render(
        request,
        "catalog_items.html",
        context={
            "items": items,
            "items_offset": items_offset,
        },
    )
