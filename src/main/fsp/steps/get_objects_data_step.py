import queue

files_queue = queue.Queue()


def execute(**params):
    import threading

    path = params.get("path", "")
    object_ids = params.get("ids", [])
    schema = params.get("object_or_schema", "")
    render = params.get("render", False)

    files = []

    if not object_ids:
        thread_files = threading.Thread(target=get_files, args=(path,))
        thread_files.start()
    else:
        thread_verif = threading.Thread(target=verif, args=(path, object_ids))
        thread_verif.start()

    if render:
        render_queue = queue.Queue()
        thread_render = threading.Thread(target=render_json, args=(schema, render_queue))
        thread_render.start()

        thread_render.join()
        return render_queue.get()

    return files


def verif(path, object_ids):
    import os.path
    global files_queue
    for (index, object_id) in enumerate(object_ids):
        s = get_file_by_id(path, object_id)
        if os.path.isfile(s):
            files_queue.put(s)
    files_queue.put(None)


def get_file_by_id(path, object_id):
    return path + "/" + str(object_id) + ".json"


def get_files(path):
    import os
    global files_queue
    [files_queue.put(path + "/" + file_name) for file_name in os.listdir(path)]
    files_queue.put(None)


def render_json(schema, result_queue):
    from src.main.fsp.json_loader import json_loader
    global files_queue
    json = "["
    loader = json_loader.load if schema is None else json_loader.load_with_schema
    file = files_queue.get()
    while file is not None:
        json += loader(path=file, schema=schema) + ","
        file = files_queue.get()
    if len(json) > 1:
        json = json[:-1]
    json += "]"
    result_queue.put(json)
