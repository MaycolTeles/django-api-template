"""
Module for providing a base admin class for all the Django models admin.

This module exports the BaseAdmin class and FieldsetType type alias.
"""

__all__ = [
    "BaseAdmin",
    "FieldsetType",
]


from .base_admin import BaseAdmin, FieldsetType
