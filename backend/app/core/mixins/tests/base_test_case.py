"""
Base test case for all test cases in the project.

This module defines a `BaseTestCase` class that provides common functionality
for all the non-API test cases in the project.

For API test cases, use the `BaseAPITestCase` class in the `base_api_test_case.py` module.
"""

from django.test import TestCase


class BaseTestCase(TestCase):
    """
    Base Test Case class containing common attributes and methods for all test cases.

    This class defines the method to create a user to be used in any test cases.

    Methods:
    -------
        * `create_user`: Method to create a user.
    """

    # Importing User here to avoid needing to use type checking.
    from account.models import User

    def create_user(self, *args, **kwargs) -> "User":
        """
        Create a user instance.

        This method creates a user instance using the `mixer` library.
        Additional arguments and keyword arguments can be passed to the method to customize the user instance.
        """
        # Importing mixer here to avoid needing to add it as a production dependency.
        from mixer.backend.django import mixer

        user = mixer.blend("account.User", *args, **kwargs)
        return user  # type: ignore
