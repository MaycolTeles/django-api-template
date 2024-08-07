"""
Base model module for Django models.

This module defines a `BaseModel` class that provides common fields for all models.
"""

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    Base Model class to add some common fields to all models.

    Fields:
    -----------
    * `id` : `UUIDField`
        To be used as the primary key.

    * `created_at` : `DateTimeField`
        To store the date and time of creation.

    * `updated_at` : `DateTimeField`
        To store the date and time of the last update.
    """

    id = models.UUIDField(
        _("ID"),
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        help_text=_("The unique identifier of the record."),
    )
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        help_text=_("The date and time the record was created."),
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
        help_text=_("The date and time the record was last updated."),
    )

    class Meta:
        abstract = True
        ordering = ("-created_at",)
