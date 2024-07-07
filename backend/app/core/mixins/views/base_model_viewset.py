"""
Module containing the BaseModelViewSet class.
"""

from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):
    """
    Base ViewSet class to be used by all other ViewSets in the app.

    This class is responsible for filtering the queryset based on the user who is making the request.
    """

    queryset: QuerySet

    def get_queryset(self):
        from account.models import User

        user: User = self.request.user  # type: ignore

        if user.is_superuser:
            return self.queryset.all()

        return self.queryset.filter(user=user)
