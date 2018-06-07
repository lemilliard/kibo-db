import os

from ...client import modules_dir
from ...client import get_module_name


def get_style_files(module_list: list):
    style_files = []
    for module in module_list:
        file = module + "/" + get_module_name(module) + ".css"
        if os.path.exists(os.path.join(modules_dir, file)):
            style_files.append(file)
    return style_files


def get_page_name(page_name):
    return page_name + " - " + data["base_page_name"]


def switch_night_mode():
    data["night_mode"] = not data["night_mode"]
    return "OK"


data = {
    "base_page_name": "ManoucheQL",
    "main_menu": [
        {"name": "Home", "path": "/home"},
        {"name": "Databases", "path": "/databases"}
    ],
    "night_mode": True,
    "current_page": ""
}

methods = {
    "get_page_name": get_page_name,
    "get_style_files": get_style_files
}

on_open = []
