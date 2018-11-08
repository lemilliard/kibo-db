def execute(**params):
    path = params.get("path", "")
    object_ids = params.get("ids", [])
    schema = params.get("object_or_schema", "")
    render = params.get("render", False)

    files = []

    if not object_ids:
        files = get_files(path)
    else:
        for object_id in object_ids:
            files.append(get_file_by_id(path, object_id))

    if render:
        if not object_ids:
            return render_json(files, schema)
        else:
            return try_render_json(files, schema)

    return files


def get_file_by_id(path, object_id):
    return path + "/" + str(object_id) + ".json"


def get_files(path):
    import os
    return [path + "/" + file_name for file_name in os.listdir(path)]


def render_json(files, schema):
    from src.main.fsp.json_loader import json_loader
    json = "["
    loader = json_loader.load if schema is None else json_loader.load_with_schema
    for file in files:
        json += loader(path=file, schema=schema) + ","
    if len(json) > 1:
        json = json[:-1]
    json += "]"
    return json


def try_render_json(files, schema):
    from src.main.fsp.json_loader import json_loader
    json = "["
    loader = json_loader.load if schema is None else json_loader.load_with_schema
    for file in files:
        try:
            json += loader(path=file, schema=schema) + ","
        except IOError:
            pass
    if len(json) > 1:
        json = json[:-1]
    json += "]"
    return json
