def execute(request):
    (url, body) = split_request(request)
    (content, details) = split_body(body)
    splitted_url = split_url(url)

    verb = splitted_url.__getitem__(0)
    ss1_result = sous_step_1(verb, content, details)
    render = verb == "read"

    for (object_or_schema, condition) in ss1_result:
        (path, routes) = sous_step_2(splitted_url, condition)
        (route_function, init_function, touch_function, next_function) = routes

        params = {
            "object_or_schema": object_or_schema,
            "path": path,
            "init_function": init_function,
            "touch_function": touch_function,
            "next_function": next_function,
            "render": render
        }

        if condition is not None:
            ids = condition.get("ids", None)
            if ids is not None and len(ids) > 0:
                params["ids"] = ids
            else:
                params["condition"] = condition

        yield route_function(**params)
    return False


def split_request(request):
    return request.get("url", None), request.get("body", None)


def split_body(body):
    return body.get("content", None), body.get("details", None)


def split_url(url):
    url_parts = url.split("/")
    return url_parts[0], url_parts[1], url_parts[2]


def sous_step_1(verb, content, details):
    if (content is not None) ^ (details is not None):
        if content is not None:
            if verb in ["create", "update", "delete"]:
                if isinstance(content, list):
                    for c in content:
                        yield get_object(c), get_condition(c)
                else:
                    yield get_object(content), get_condition(content)
            else:
                raise Exception("L'action " + verb + " ne peut pas contenir le champs 'content'")
        elif verb == "read":
            yield get_schema(details), get_condition(details)
        else:
            raise Exception("L'action " + verb + " ne peut pas contenir le champs 'details'")
    else:
        raise Exception("Une requête ne peut contenir les champs 'content' et 'details' en même temps")


def get_object(content):
    return content.get("object", None)


def get_schema(details):
    return details.get("schema", None)


def get_condition(content_details):
    return content_details.get("condition", None)


def get_path(database, table):
    return "../../../../databases/" + database + "/" + table + "/data"


def sous_step_2(splitted_url, condition):
    (verb, database, table) = splitted_url
    return get_path(database, table), define_routes(verb, condition)


def define_routes(verb, condition):
    routes = (None, None, None, None)
    is_by_id = False
    if condition is not None:
        ids = condition.get("ids", None)
        is_by_id = ids is not None and len(ids) > 0
    if is_by_id or condition is None:
        from src.main.fsp.steps import get_objects_data_step
        init_function = get_objects_data_step.execute
    else:
        from src.main.fsp.steps import get_by_condition_step
        init_function = get_by_condition_step.execute

    if verb == "read":
        routes = (init_function, None, None, None)
    elif verb == "create":
        from src.main.fsp.steps import create_data_step
        routes = (create_data_step.execute, None, None, None)
    elif verb == "update" or verb == "delete":
        from src.main.fsp.steps import touch_data_step
        from src.main.fsp.functions import touch_functions
        from src.main.fsp.functions import indexes_functions
        touch_function = None
        next_function = None
        if verb == "update":
            touch_function = touch_functions.update_file
            next_function = indexes_functions.update_indexes
        elif verb == "delete":
            touch_function = touch_functions.delete_file
            next_function = indexes_functions.delete_indexes
        routes = (touch_data_step.execute, init_function, touch_function, next_function)
    return routes


req = {
    "url": "read/test/user",
    "body": {
        # "content": [
        #     {"object": {}, "condition": {"ids": [1]}},
        #     {"object": {}, "condition": {}},
        #     {"object": {}, "condition": {}}
        # ],
        "details": {"schema": "{"
                              "liste_objets: {id, sous_objet: {id}}, "
                              "sous_objet: "
                              "{"
                              "id, "
                              "liste_objets: {id,sous_objet: {id}}, "
                              "sous_objet: {id}"
                              "}"
                              "}", "condition": {"ids": [3]}}
    }
}

result = execute(req)

for r in result:
    print(r)
