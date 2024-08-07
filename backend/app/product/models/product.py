"""
Module containing the Product model.
"""

from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import User
from core.mixins import BaseModel


class Product(BaseModel):
    """
    Model to store some product-related data.

    This model is used to store some product-related data.

    Fields:
    -----------
        * `user`: `ForeignKey[User]`
            The user who created the product

        * `name`: `str`
            The name of the product

        * `description`: `str`
            The description of the product

        * `price`: `Decimal`
            The price of the product
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("User"),
        help_text=_("The user who created the product."),
    )
    name = models.CharField(
        _("Name"),
        max_length=255,
        help_text=_("The name of the product."),
    )
    description = models.TextField(
        _("Description"),
        default="",
        help_text=_("The description of the product (optional)."),
    )
    price = models.DecimalField(
        _("Price"),
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal(0.0))],
        help_text=_("The price of the product. Must be greater than or equal to 0."),
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
