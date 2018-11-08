import queue

q = queue.Queue()

def execute(**params):
    import threading

    path = params.get("path", "")
    object_ids = params.get("ids", [])
    schema = params.get("object_or_schema", "")
    render = params.get("render", False)

    files = []

    if not object_ids:
        files = get_files(path)
    else:
        thread_verif = threading.Thread(verif(path, object_ids))
        thread_verif.start()
        thread_verif.join()

    if render:
        if not object_ids:
            return render_json(files, schema)
        else:
            render_queue = queue.Queue()
            thread_render = threading.Thread(try_render_json(schema, render_queue))
            thread_render.start()
            thread_render.join()
            return render_queue.get()

    return files

def verif(path, object_ids):
    import os.path
    global q
    for object_id in object_ids:
        s = get_file_by_id(path, object_id)
        if os.path.isfile(s):
            q.put(s)
            print(s)
    q.put(None)



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


def try_render_json(schema, result_queue):
    from src.main.fsp.json_loader import json_loader
    global q
    json = "["
    loader = json_loader.load if schema is None else json_loader.load_with_schema
    file = q.get()
    while file is not None:
        print(file)
        try:
            json += loader(path=file, schema=schema) + ","
        except IOError:
            pass
        file = q.get()
    if len(json) > 1:
        json = json[:-1]
    json += "]"
    result_queue.put(json)
