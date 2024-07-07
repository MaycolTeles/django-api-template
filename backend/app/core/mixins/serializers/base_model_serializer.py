"""
Module containing the BaseModelSerializer class.
"""

from rest_framework.serializers import ModelSerializer


class BaseModelSerializer(ModelSerializer):
    """ """

    class Meta:
        abstract = True
        fields = "__all__"
