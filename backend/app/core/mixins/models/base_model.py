"""
Module containing the BaseModel class.
"""

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    Class to add the following fields to all models that inherit from it:

    `id` : `UUIDField`
        To be used as the primary key.

    `created_at` : `DateTimeField`
        To store the date and time of creation.

    `updated_at` : `DateTimeField`
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
        ordering = ('-created_at',)
