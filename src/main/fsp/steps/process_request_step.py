def execute(request):
    (url, body) = sous_step_1(request)
    ss2_result = sous_step_2(url, body)

    (obj, schema, condition, path, routes) = ss2_result
    params = {}
    if obj is not None:
        params['object'] = obj
    if schema is not None:
        params['schema'] = schema
    if condition is not None:
        params['condition'] = condition
    if path is not None:
        params['path'] = path
    if routes is not None:
        (route_function, init_function, touch_function, next_function) = routes
        params['init_function'] = init_function
        params['touch_function'] = touch_function
        params['next_function'] = next_function
        return route_function(**params)
    return False


def sous_step_1(request):
    return split_request(request)


def split_request(request):
    return 'create/kibo_cloud/user', {}


def sous_step_2(url, body):
    obj = get_object(body)
    schema = get_schema(body)
    condition = get_condition(body)
    (verb, database, table) = split_url(url)
    path = get_path(database, table)
    return \
        obj, \
        schema, \
        condition, \
        path, \
        define_routes(verb, condition)


def get_object(body):
    return {}


def get_schema(body):
    return ''


def get_condition(body):
    return {}


def get_path(database, table):
    return database + '/' + table


def define_routes(verb, condition):
    routes = (None, None, None, None)
    ids = condition.get('ids', None)
    is_by_id = ids is not None and len(ids) > 0
    if is_by_id:
        from src.main.fsp.steps import get_objects_data_step
        init_function = get_objects_data_step.execute
    else:
        from src.main.fsp.steps import find_by_index_step
        init_function = find_by_index_step.execute

    if verb == 'read':
        routes = (init_function, None, None, None)
    elif verb == 'create':
        from src.main.fsp.steps import create_data_step
        routes = (create_data_step.execute, None, None, None)
    elif verb == 'update' or verb == 'delete':
        from src.main.fsp.steps import touch_data_step
        from src.main.fsp.functions import touch_functions
        from src.main.fsp.functions import indexes_functions
        touch_function = None
        next_function = None
        if verb == 'update':
            touch_function = touch_functions.update_file
            next_function = indexes_functions.update_indexes
        elif verb == 'delete':
            touch_function = touch_functions.delete_file
            next_function = indexes_functions.delete_indexes
        routes = (touch_data_step.execute, init_function, touch_function, next_function)
    return routes


def split_url(url):
    url_parts = url.split('/')
    return url_parts[0], url_parts[1], url_parts[2]


execute(None)
