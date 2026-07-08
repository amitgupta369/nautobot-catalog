from nautobot.apps.models import PrimaryModel
from django.db import models


class CatalogPlugin(PrimaryModel):
    SECTION_CHOICES = (
        ("private", "Private"),
        ("public", "Public"),
    )

    name = models.CharField(max_length=100, unique=True)

    vendor = models.CharField(
        max_length=100,
        blank=True,
    )

    section = models.CharField(
        max_length=20,
        choices=SECTION_CHOICES,
        default="private",
    )

    icon = models.CharField(
        max_length=100,
        default="mdi mdi-package-variant",
    )

    url = models.CharField(
        max_length=255,
    )

    weight = models.PositiveIntegerField(
        default=100,
    )

    enabled = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["section", "weight", "name"]

    def __str__(self):
        return self.vendor or self.name