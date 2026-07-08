from nautobot_catalog.models import CatalogPlugin


class CatalogService:

    @classmethod
    def get_plugins(cls):
        return CatalogPlugin.objects.filter(
            enabled=True
        ).order_by(
            "section",
            "weight",
            "name",
        )