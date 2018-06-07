import os
import importlib
import importlib.util

from flask import render_template

from . import router

modules_dir = "./client_old/modules"
modules_package = "src.client_old.modules"
common_modules = ["base", "header", "footer"]


def client_endpoint(url=None):
    url_params = []
    if url != "" and url is not None:
        route = router.get_route_by_url(url)
        url_params = router.get_url_params(url, route["path"])
    else:
        route = router.get_default_route()

    if not is_route_valid(route):
        route = router.get_default_route()

    module_full_name = route["module"]
    module_path = module_full_name + "/" + get_module_name(module_full_name)
    html = module_path + ".html.jinja2"

    module_controller = get_module_controller(module_full_name)
    module_full_controller = get_full_module_controller(module_controller)

    execute_on_open(module_full_controller)
    methods = module_full_controller["methods"]
    data = module_full_controller["data"]

    return render_template(
        "base/base.html.jinja2",
        module_list=common_modules + [module_full_name],
        html=html,
        data=data,
        methods=methods,
        params=url_params
    )


def get_full_module_controller(module_controller):
    module_full_controller = dict()
    if module_controller is not None:
        module_full_controller = module_controller.__dict__

    if not hasattr(module_controller, "data"):
        module_full_controller["data"] = dict()
    if not hasattr(module_controller, "methods"):
        module_full_controller["methods"] = dict()
    if not hasattr(module_controller, "on_open"):
        module_full_controller["on_open"] = []

    for common_module in common_modules:
        common_module_controller = get_module_controller(common_module)
        if hasattr(common_module_controller, "data"):
            module_full_controller["data"].update(common_module_controller.data)

        if hasattr(common_module_controller, "methods"):
            module_full_controller["methods"].update(common_module_controller.methods)
    return module_full_controller


def get_module_controller(module_full_name):
    module_controller = None
    if does_module_exist(module_full_name):
        module_name = module_full_name.replace("/", ".")
        module_name = "." + module_name
        module_simple_name = get_module_name(module_full_name)
        module_simple_name = "." + module_simple_name
        if importlib.util.find_spec(module_simple_name, modules_package + module_name):
            module_controller = importlib.import_module(module_simple_name, modules_package + module_name)
    return module_controller


def execute_on_open(module_controller):
    for on_open_method in module_controller["on_open"]:
        if on_open_method in module_controller["methods"]:
            module_controller["methods"][on_open_method]()


def does_module_exist(module) -> bool:
    exist = False
    if os.path.isdir("../src/client_old/modules/" + module):
        exist = True
    return exist


def is_route_valid(route) -> bool:
    valid = False
    module_path = route["module"] + "/" + get_module_name(route["module"])
    html = module_path + ".html.jinja2"
    py = module_path + ".py"
    if os.path.exists(os.path.join(modules_dir, html)) and os.path.exists(os.path.join(modules_dir, py)):
        valid = True
    return valid


def get_module_name(module_full_name):
    module_full_name_parts = module_full_name.split("/")
    return module_full_name_parts[len(module_full_name_parts) - 1]
