def execute(**params):
    path = params.get("path", "")
    object_ids = params.get("ids", [])
    schema = params.get("object_or_schema", "")
    render = params.get("render", False)

    files = []

    for object_id in object_ids:
        files.append(get_file_by_id(path, object_id))

    if render:
        return render_json(files, schema)

    return files


def get_file_by_id(path, object_id):
    return path + "/" + str(object_id) + ".json"


def render_json(files, schema):
    from src.main.fsp.json_loader import json_loader
    json = ""
    for (index, file) in enumerate(files):
        try:
            if index > 0:
                json += ","
            json += json_loader.load(file, schema)
        except IOError:
            pass
    return json
