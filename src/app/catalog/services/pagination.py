from typing import NamedTuple

from django.http import HttpRequest
from django.contrib.postgres.search import SearchQuery, SearchVector

from ..models import Product


_DEFAULT_PAGE_SIZE = 20


class PageInfo(NamedTuple):
    page: int
    page_size: int


def get_page_info_from_request(request: HttpRequest):
    page = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", _DEFAULT_PAGE_SIZE)
    return PageInfo(int(page), int(page_size))


def get_paginated_products(page_info: PageInfo, search_query: str | None = None):
    start = (page_info.page - 1) * page_info.page_size
    end = start + page_info.page_size

    if search_query:
        search_vectors = SearchVector("name") + SearchVector("description")
        products = Product.objects.annotate(
            search=search_vectors,
        ).filter(
            search=SearchQuery(search_query)
        )[start:end]

    else:
        products = Product.objects.all()[start:end]
    return products
