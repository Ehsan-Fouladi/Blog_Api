from rest_framework.pagination import PageNumberPagination
from django.conf import settings


class StandardResultSetPagination(PageNumberPagination):
    page_size = getattr(settings, 'PAGINATION_PAGE_SIZE', 9)


class PostResultSetPagination(PageNumberPagination):
    page_size = getattr(settings, 'PAGINATION_PAGE_SIZE', 3)


class SearchResultSetPagination(PageNumberPagination):
    page_size = getattr(settings, 'PAGINATION_PAGE_SIZE', 6)
