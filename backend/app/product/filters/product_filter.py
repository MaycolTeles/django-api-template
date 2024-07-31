"""
Module containing the Product FilterSet.
"""

from django_filters import rest_framework as filters

from product.models import Product


class ProductFilter(filters.FilterSet):
    """
    Class to filter the Product model.
    """

    name = filters.CharFilter(field_name="name", lookup_expr="icontains", label="Name Contains")
    description = filters.CharFilter(field_name="description", lookup_expr="icontains", label="Description Contains")

    price__lt = filters.NumberFilter(field_name="price", lookup_expr="lt", label="Price Less Than")
    price__lte = filters.NumberFilter(field_name="price", lookup_expr="lte", label="Price Less Than or Equal To")
    price__gte = filters.NumberFilter(field_name="price", lookup_expr="gte", label="Price Greater Than or Equal To")
    price__gt = filters.NumberFilter(field_name="price", lookup_expr="gt", label="Price Greater Than")

    ordering = filters.OrderingFilter(
        fields=(
            ("name", "name"),
            ("price", "price"),
        ),
    )

    class Meta:
        model = Product
        fields = ("name", "description", "price")
