"""
Module containing the User admin.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import User
from core.mixins import BaseAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin, BaseAdmin):
    """
    Admin class for the User model.
    """

    search_fields = (
        "email",
        "username",
        "first_name",
    )
    list_display = ("username", "email")
