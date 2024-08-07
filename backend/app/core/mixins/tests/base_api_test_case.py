"""
Base API test module for API tests.

This module defines a `BaseAPITestCase` class that provides common functionality
for API tests.

For non-API test cases, use the `BaseTestCase` class in the `base_test_case.py` module.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework.test import APIClient, APITestCase

from core.mixins.tests.base_test_case import BaseTestCase


if TYPE_CHECKING:
    from account.models import User


class BaseAPITestCase(APITestCase, BaseTestCase):
    """
    Base API Test Case class containing common attributes and methods for all API test cases.

    This class defines common attributes and methods for all API test cases.
    It also provides a method to login the user.

    Attributes
    -------------
        * `user` : `User`
            The user instance.

        * `user_id` : `str`
            The user ID.

    Methods
    ----------
        * `setUp`: Method to set up the test case. This method runs before every test case.
        * `login`: Method to login the user.
    """

    user: User
    user_id: str

    def setUp(self) -> None:
        """
        Set up the test case by creating a user instance.

        This method creates a user instance and sets the user and user ID attributes.
        """
        self.user = self.create_user()
        self.user_id = str(self.user.id)

    def login(self) -> None:
        """
        Logs in the user.

        This method logs in the user using the APIClient by force authenticating the user.
        """
        client: APIClient = self.client  # type: ignore
        client.force_authenticate(user=self.user)
