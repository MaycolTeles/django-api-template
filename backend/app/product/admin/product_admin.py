"""
Module containing the Product admin.
"""

from django.contrib import admin

from core.mixins import BaseAdmin
from product.models import Product


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    """
    Admin class for the Product model.
    """

    search_fields = (
        "name",
        "description",
        "price",
    )
    list_display = ("name", "description", "price")
