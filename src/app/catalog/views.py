from django.shortcuts import render
from django.http import HttpRequest

from .services.pagination import get_paginated_products, get_page_info_from_request


def index(request):
    return render(
        request,
        "catalog.html",
    )


def paginated_items_view(request: HttpRequest):
    # get query params
    page_info = get_page_info_from_request(request)
    search_query = request.GET.get("search", None)

    products = get_paginated_products(page_info, search_query)

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
