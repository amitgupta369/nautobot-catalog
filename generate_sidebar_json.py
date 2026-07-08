import json
import importlib

from django.apps import apps

try:
    from nautobot.extras.plugins import NautobotAppConfig
except ImportError:
    from nautobot.apps import NautobotAppConfig


OUTPUT_FILE = "sidebar.json"


def load_navigation_module(app_config):
    """
    Import <app>.navigation if present.
    """
    try:
        return importlib.import_module(
            f"{app_config.name}.navigation"
        )
    except Exception:
        return None


def get_navigation_objects(app_config):
    """
    Return navigation objects from navigation.py
    """
    navigation = load_navigation_module(app_config)

    if not navigation:
        return []

    return (
        getattr(navigation, "home_sidebar_items", None)
        or getattr(navigation, "menu_items", None)
        or getattr(app_config, "home_sidebar_items", None)
        or getattr(app_config, "menu_items", None)
        or []
    )


def normalize_groups(nav_objects):
    """
    Convert:
        NavMenuTab -> groups
        NavMenuGroup -> group
    into a flat list of groups.
    """
    groups = []

    for obj in nav_objects:
        # NavMenuTab
        if hasattr(obj, "groups"):
            groups.extend(obj.groups or [])

        # NavMenuGroup
        elif hasattr(obj, "items"):
            groups.append(obj)

    return groups


def build_sidebar_entry(app_config, group):
    return {
        "app": app_config.name,
        "plugin": app_config.verbose_name,
        "group": group.name,
        "icon": getattr(
            app_config,
            "vendor_icon",
            "bi-puzzle",
        ),
        "section": getattr(
            app_config,
            "home_sidebar_section",
            "private",
        ),
        "items": [
            {
                "name": item.name,
                "link": item.link,
                "weight": getattr(item, "weight", 1000),
            }
            for item in getattr(group, "items", [])
        ],
    }


def generate_sidebar_json():
    sidebar = []

    for app_config in sorted(
        apps.get_app_configs(),
        key=lambda x: x.verbose_name.lower(),
    ):
        print(f"Processing: {app_config.name}")

        nav_objects = get_navigation_objects(
            app_config
        )

        if not nav_objects:
            continue

        groups = normalize_groups(nav_objects)

        for group in groups:
            sidebar.append(
                build_sidebar_entry(
                    app_config,
                    group,
                )
            )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            sidebar,
            f,
            indent=4,
            ensure_ascii=False,
            sort_keys=False,
        )

    print(
        f"\nGenerated {OUTPUT_FILE}"
    )
    print(
        f"Total groups: {len(sidebar)}"
    )


if __name__ == "__main__":
    generate_sidebar_json()