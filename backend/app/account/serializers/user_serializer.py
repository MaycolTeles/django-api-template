"""
Module containing the User serializer.
"""

from rest_framework import serializers

from account.models import User
from core.mixins import BaseModelSerializer


class UserSerializer(BaseModelSerializer):
    """
    Class to serialize the User model.
    """

    class Meta:
        model = User
        exclude = ["password"]
