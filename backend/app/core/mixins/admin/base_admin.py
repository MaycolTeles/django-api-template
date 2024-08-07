"""
Base admin module for Django models.

This module defines a `BaseAdmin` class that provides common functionality
for handling readonly fields and fieldsets in the Django admin interface.
"""

from django.contrib.admin import ModelAdmin
from django.db.models import Model
from django.http import HttpRequest


FieldsetType = tuple[str, dict[str, list[str]]]


BASE_FIELDS = ["id", "created_at", "updated_at"]


class BaseAdmin(ModelAdmin):
    """
    Base Admin class containing common attributes and methods for all admin classes.

    This class defines common attributes and methods for all admin classes.
    It also ensures that some base fields (such as "id", "created_at", and "updated_at")
    are always displayed as readonly fields in the admin interface.
    """

    def get_readonly_fields(self, request: HttpRequest, obj: Model) -> list[str]:
        """
        Get the list of fields that are readonly in the admin interface.

        This method gets the list of fields that are readonly from the superclass and then
        extend the list by including the base fields.

        Args
        ----------
            * `request`: The HttpRequest object.
            * `obj`: The model instance.

        Returns
        ----------
            A list of readonly field names.
        """
        readonly_fields = super().get_readonly_fields(request, obj)
        return BASE_FIELDS + list(readonly_fields)

    def get_fieldsets(self, request: HttpRequest, obj: Model) -> list[FieldsetType]:
        """
        Get the fieldsets for the admin interface.

        This method gets the fieldsets from the superclass and then extends the fieldsets
        by adding the base fields to the base fieldset.

        Args
        ----------
            * `request`: The HttpRequest object.
            * `obj`: The model instance.

        Returns
        ----------
            A list of fieldsets for the model admin, including the base fieldset
            that contains the base fields and the default fieldset.
        """
        fieldsets = super().get_fieldsets(request, obj)

        # Removing base fields from the fieldsets, since they are already in the base fieldset
        base_fields = [field for field in fieldsets[0][1]["fields"] if field not in BASE_FIELDS]
        additional_fieldsets: list[FieldsetType] = fieldsets[1:]  # type: ignore

        all_fieldsets = [
            self._get_base_fieldset(),
            self._get_default_fieldset(base_fields),
            *additional_fieldsets,
        ]
        return all_fieldsets

    def _get_base_fieldset(self) -> FieldsetType:
        """
        Get the base fieldset containing the base fields.

        This method returns a fieldset containing all the base fields
        that are always displayed in the admin interface.

        Returns
        ----------
            A fieldset containing the base fields.
        """
        return (
            "Base Fields",
            {
                "fields": BASE_FIELDS,
            },
        )

    def _get_default_fieldset(self, fields: list[str]) -> FieldsetType:
        """
        Get the default fieldsets for the admin interface.

        This method returns a fieldset containing the given fields,
        where the fieldset name is the model name in title case and
        the fields are the given fields.

        Args
        ----------
            fields: A list of field names.

        Returns
        ----------
            A fieldset containing the given fields.
        """
        fieldset_name = f"{self.model._meta.verbose_name.capitalize()} details"
        return (
            fieldset_name,
            {
                "fields": fields,
            },
        )
