from typing import Optional

from django.contrib.admin import ModelAdmin

FieldsetType = tuple[str, dict[str, list[str]]]


class BaseAdmin(ModelAdmin):
    """
    Base Admin class.

    This class defines common attributes and methods for all admin classes.
    """

    fields_in_fieldset_already: Optional[list[str]] = None

    def get_readonly_fields(self, request, obj) -> list[str]:
        readonly_fields = super().get_readonly_fields(request, obj)
        return ["id", "created_at", "updated_at"] + list(readonly_fields)

    def get_fieldsets(self, request, obj) -> list[FieldsetType]:
        """
        Method to get the fieldsets for the admin.
        """
        all_fieldsets = super().get_fieldsets(request, obj)
        base_fields = all_fieldsets[0][1]["fields"]
        additional_fieldsets = all_fieldsets[1:]
        base_fieldset = self.get_base_fieldset(base_fields)

        id_fieldset = self.get_id_fieldset()
        fieldsets = [id_fieldset, base_fieldset, *additional_fieldsets]

        return fieldsets

    def get_id_fieldset(self) -> FieldsetType:
        return (
            "ID",
            {
                "fields": ["id", "created_at", "updated_at"],
            },
        )

    def get_base_fieldset(self, fields: list[str]) -> FieldsetType:
        try:
            # Removing the "id", "created_at", "updated_at" fields since
            # they have a dedicated fieldset
            fields.remove("id")
            fields.remove("created_at")
            fields.remove("updated_at")

            # Removing the fields that are already in a fieldset
            f = self.fields_in_fieldset_already
            if f:
                for field in f:
                    fields.remove(field)

        except Exception:
            # If the fields are not in the list, just pass
            pass

        fieldset_name = f"{self.model._meta.verbose_name} details"
        return (
            fieldset_name,
            {
                "fields": fields,
                # "classes": ["collapse"],
            },
        )
