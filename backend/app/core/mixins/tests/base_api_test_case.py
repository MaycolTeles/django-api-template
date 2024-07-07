"""
Module containing the BaseAPITestCase class.
"""

from rest_framework.test import APIClient, APITestCase

from core.mixins.tests.base_test_case import BaseTestCase


class BaseAPITestCase(APITestCase, BaseTestCase):
    """ """

    def setUp(self):
        """
        Method to set up the test case.
        """
        self.user = self.create_user()
        self.user_id = str(self.user.id)

    def login(self):
        """
        Method to login the user by force authenticating the client.
        """
        client: APIClient = self.client  # type: ignore
        client.force_authenticate(user=self.user)
