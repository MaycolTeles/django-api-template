"""
Module containing the Product serializer.
"""

from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Class to serialize the Product model.
    """

    class Meta:
        model = Product
        fields = "__all__"
