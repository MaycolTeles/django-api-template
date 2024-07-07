"""
Module containing the Product views.
"""

from core.mixins import BaseModelViewSet
from product.filters import ProductFilter
from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(BaseModelViewSet):
    """
    API endpoint to define Product actions/methods.

    The available actions for the Product model are:
    * List
    * Create
    * Retrieve
    * Update
    * Destroy
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
