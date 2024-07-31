"""
Module containing the Account app configuration.
"""

from django.apps import AppConfig


class AccountConfig(AppConfig):
    """
    Class containing the Account app configuration.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "account"
