import json
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.static import serve
from django.http import Http404

from .models import TelegramUser
from .services.pagination import get_paginated_products, get_page_info_from_request
from app.settings import ASSETS_ROOT


def index(request):

    user_query = request.GET.get("user")
    if user_query:
        user_obj: dict = json.loads(user_query)
        user = TelegramUser.objects.filter(
            telegram_id=user_obj.get("id")).first()
        if not user:
            user = TelegramUser.objects.create(
                telegram_id=user_obj.get("id"),
                first_name=user_obj.get("first_name"),
                last_name=user_obj.get("last_name"),
                username=user_obj.get("username"),
                language_code=user_obj.get("language_code"),
            )

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
            "id": product.id,
            "liked": product.id,
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


def serve_images(request: HttpRequest, path: str, document_root: str):
    try:
        response = serve(request, path, document_root)
    except Http404:
        response = serve(request, "img-placeholder.webp", ASSETS_ROOT)
    return response
