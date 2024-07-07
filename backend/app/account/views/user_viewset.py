"""
Module containing the User views.
"""

from account.models import User
from account.serializers import UserSerializer
from core.mixins import BaseModelViewSet


class UserViewSet(BaseModelViewSet):
    """
    API endpoint to define User actions.

    The available actions for the User model are:
    * List
    * Create
    * Retrieve
    * Update
    * Destroy
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
