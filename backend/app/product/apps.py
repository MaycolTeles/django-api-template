"""
Module for product app configuration.
"""

from django.apps import AppConfig


class ProductConfig(AppConfig):
    """
    Product app configuration class.

    This class defines the configuration for the product app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "product"
