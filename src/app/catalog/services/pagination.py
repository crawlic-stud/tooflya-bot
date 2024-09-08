from typing import NamedTuple

from django.http import HttpRequest

from ..models import Product


_DEFAULT_PAGE_SIZE = 20


class PageInfo(NamedTuple):
    page: int
    page_size: int


def get_page_info_from_request(request: HttpRequest):
    page = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", _DEFAULT_PAGE_SIZE)
    return PageInfo(int(page), int(page_size))


def get_paginated_products(page_info: PageInfo):
    start = (page_info.page - 1) * page_info.page_size
    end = start + page_info.page_size

    products = Product.objects.all()[start:end]
    return products
