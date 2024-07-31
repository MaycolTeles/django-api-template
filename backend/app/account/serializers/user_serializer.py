"""
Module containing the User serializer.
"""

from rest_framework import serializers

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Class to serialize the User model.
    """

    class Meta:
        model = User
        exclude = ["password"]
