import re

routes = [
    {"name": "Home", "path": "home", "module": "home"},
    {"name": "Databases", "path": "database", "module": "database/databases"},
    {"name": "Database", "path": "database/{system_name}", "module": "database/database"},
    {"name": "Test", "path": "sub/test", "module": "test"},
]


def get_default_route():
    return routes[0]


def get_route_by_url(url: str):
    for route in routes:
        if does_url_matches_path(url, route["path"]):
            return route
    return get_default_route()


def does_url_matches_path(url: str, path: str):
    match = False
    url_parts = get_url_parts(url)
    path_parts = get_url_parts(path)
    if len(url_parts) == len(path_parts):
        match = True
        i = 0
        while i < len(url_parts) and match:
            if url_parts[i] != path_parts[i]:
                if not is_param(path_parts[i]):
                    match = False
            i += 1
    return match


def get_url_parts(url: str):
    url_parts = []
    for url_part in url.split("/"):
        if url_part != "" and url_part is not None:
            url_parts.append(url_part)
    return url_parts


def is_param(url_part: str):
    return re.match("{(.*?)}", url_part, re.DOTALL)


def get_path_params(path: str):
    return re.findall("{(.*?)}", path, re.DOTALL)


def get_url_params(url: str, path: str):
    url_params = {}
    url_parts = get_url_parts(url)
    path_parts = get_url_parts(path)
    if len(url_parts) == len(path_parts):
        match = True
        i = 0
        while i < len(url_parts) and match:
            if url_parts[i] != path_parts[i]:
                if is_param(path_parts[i]):
                    key = re.sub("[{}]", "", path_parts[i])
                    value = url_parts[i]
                    url_params[key] = value
            i += 1
    return url_params
