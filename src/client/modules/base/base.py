from ...client import modules_dir


def get_style_file(module_name):
    file = modules_dir + "/" + module_name + "/" + module_name + ".css"
    return file


def get_page_name(page_name):
    return page_name + " - " + data["base_page_name"]


def switch_night_mode():
    data["night_mode"] = not data["night_mode"]
    return "OK"


data = {
    "base_page_name": "ManoucheQL",
    "main_menu": [
        {"name": "Home", "path": "/home"},
        {"name": "Databases", "path": "/database"}
    ],
    "night_mode": True,
    "current_page": ""
}

methods = {
    "get_page_name": get_page_name,
    "get_style_file": get_style_file
}

on_open = []
