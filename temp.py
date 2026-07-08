
import json
import sys
import importlib

from django.apps import apps

try:
    from nautobot.extras.plugins import NautobotAppConfig
except ImportError:
    from nautobot.apps import NautobotAppConfig

for app_config in apps.get_app_configs():

    print("-" * 50)
    app_name = app_config.name
    is_menu_tabs = getattr(app_config.__class__, "menu_tabs", None)
    print(f"{app_name}: {is_menu_tabs}")
    if is_menu_tabs:
        try:
            sub_mod = importlib.import_module(f"{app_name}.navigation")
            print(getattr(sub_mod, "menu_items", None))
        except:
            print("test")

