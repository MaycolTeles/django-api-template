"""
Module containing the BaseTestCase class.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from mixer.backend.django import mixer
from django.test import TestCase


if TYPE_CHECKING:
    from account.models import User


class BaseTestCase(TestCase):
    """ """

    user: User
    user_id: str

    def create_user(self, *args, **kwargs) -> User:
        """
        Method to create a user using mixer.
        """
        from account.models import User

        user: User = mixer.blend(User, *args, **kwargs)  # type: ignore
        return user
