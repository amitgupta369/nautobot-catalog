from collections import defaultdict

from nautobot.apps.ui import (
    NavMenuGroup,
    NavMenuItem,
    NavMenuTab,
)

from nautobot_catalog.services.catalog import CatalogService


class CatalogNavigationService:

    @classmethod
    def build_navigation(cls):
        plugins = CatalogService.get_plugins()

        grouped = defaultdict(list)

        for plugin in plugins:
            grouped[plugin.section].append(plugin)

        groups = []

        for section in ["private", "public"]:
            items = []

            for plugin in grouped.get(section, []):
                items.append(
                    NavMenuItem(
                        name=plugin.vendor or plugin.name,
                        link=plugin.link,
                        icon=plugin.icon,
                        weight=plugin.weight,
                    )
                )

            if items:
                groups.append(
                    NavMenuGroup(
                        name=section.title(),
                        items=tuple(items),
                    )
                )

        if not groups:
            return None

        return NavMenuTab(
            name="Network Catalog",
            groups=tuple(groups),
            weight=9000,
        )