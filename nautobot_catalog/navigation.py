from nautobot_catalog.services.navigation import (
    CatalogNavigationService,
)

catalog_tab = None #CatalogNavigationService.build_navigation()

menu_items = ()

if catalog_tab:
    menu_items = (catalog_tab,)
