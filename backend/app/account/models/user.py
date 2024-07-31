"""
Module containing the User model.
"""

from django.contrib.auth.models import AbstractUser

from core.mixins import BaseModel


class User(AbstractUser, BaseModel):
    """
    Class to represent an user.
    """

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "User"
        verbose_name_plural = "Users"
