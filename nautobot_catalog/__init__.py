"""App declaration for nautobot_vlan_request."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version("nautobot-catalog")


class NautobotCatalogConfig(NautobotAppConfig):
    """App configuration for the nautobot_catalog app."""

    name = "nautobot_catalog"
    verbose_name = "Nautobot Catalog App"
    version = __version__
    author = "Amit Gupta"
    description = "Nautobot Catalog App developed by HCLTech"

config = NautobotCatalogConfig  # pylint:disable=invalid-name