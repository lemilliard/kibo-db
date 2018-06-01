import os
import importlib
import importlib.util

from flask import render_template

from . import router

pages_dir = "pages"
common_modules = ["config", "base", "header", "footer"]


def client_endpoint(url=None):
    url_params = []
    if url != "" and url is not None:
        route = router.get_route_by_url(url)
        url_params = router.get_url_params(url, route["path"])
    else:
        route = router.get_default_route()

    module = route["module"]
    page = module + ".html.jinja2"
    if os.path.exists("../src/client/view/pages/" + page):
        methods = get_methods(module)
        execute_on_open(module, methods)
        data = get_data(module)
        return render_template(
            "base.html.jinja2",
            module=module,
            page=page,
            data=data,
            methods=methods,
            params=url_params
        )
    return "Page does not exist"


def get_data(p_module):
    data = dict()
    for module in common_modules:
        data_module = get_data_module(module)
        if data_module is not False and hasattr(data_module, "data"):
            data.update(data_module.data)
    page_data = get_data_module(pages_dir + "/" + p_module)
    if page_data is not False and hasattr(page_data, "data"):
        data.update(page_data.data)
    return data


def get_methods(p_module):
    methods = dict()
    for module in common_modules:
        data_module = get_data_module(module)
        if data_module is not False and hasattr(data_module, "methods"):
            methods.update(data_module.methods)
    page_data = get_data_module(pages_dir + "/" + p_module)
    if page_data is not False and hasattr(page_data, "methods"):
        methods.update(page_data.methods)
    return methods


def get_data_module(p_page=None):
    if p_page is not None:
        module_name = p_page.replace("/", ".")
        module_name = "." + module_name
        if importlib.util.find_spec(module_name, "src.client.data"):
            return importlib.import_module(module_name, "src.client.data")
    return False


def execute_on_open(module, methods: dict):
    on_open_methods = []
    for common_module in common_modules:
        on_open_module = get_data_module(common_module)
        if on_open_module is not False and hasattr(on_open_module, "on_open"):
            on_open_methods += on_open_module.on_open
    on_open_module = get_data_module(pages_dir + "/" + module)
    if on_open_module is not False and hasattr(on_open_module, "methods"):
        on_open_methods += on_open_module.on_open
    for on_open_method in on_open_methods:
        if on_open_method in methods:
            methods[on_open_method]()
