"""
Module containing the Product serializer.
"""

from core.mixins import BaseModelSerializer
from product.models import Product


class ProductSerializer(BaseModelSerializer):
    """
    Class to serialize the Product model.
    """

    class Meta:
        model = Product
        fields = '__all__'
