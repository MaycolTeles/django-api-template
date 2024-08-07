"""
Base ViewSet class to be used by all other ViewSets in the app.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework.viewsets import ModelViewSet


if TYPE_CHECKING:
    from django.db.models import QuerySet

    from account.models import User


class BaseModelViewSet(ModelViewSet):
    """
    Base ViewSet class to be used by all other ViewSets in the app.

    This class provides a common `get_queryset` method that filters the queryset based on the user.
    If the user is a superuser, the entire queryset is returned.

    Inheriting this class ensures that the queryset is filtered based on the user. If you don't want this behavior,
    inherit from `ModelViewSet` directly.

    Attributes:
    -------------
        * `queryset` : `QuerySet`
            The queryset to be used by the ViewSet.

    Methods:
    ----------
        * `get_queryset`: Method to get the queryset based on the user.
    """

    queryset: QuerySet

    def get_queryset(self) -> QuerySet:
        """
        Get the queryset based on the user.

        This method filters the queryset based on the user. If the user is a superuser, the entire queryset is returned.

        Returns:
        ----------
        QuerySet
            The filtered queryset based on the user.
        """
        user: User = self.request.user  # type: ignore

        if user.is_superuser:
            return self.queryset.all()

        return self.queryset.filter(user=user)
