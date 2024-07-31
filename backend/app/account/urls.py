"""
Module containing all the URL patterns for the Account app.
"""

from rest_framework import routers

from account.views import UserViewSet


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
