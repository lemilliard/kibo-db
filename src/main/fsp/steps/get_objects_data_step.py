def execute(**params):
    from multiprocessing import Process, Queue

    path = params.get("path", "")
    object_ids = params.get("ids", [])
    schema = params.get("object_or_schema", "")
    render = params.get("render", False)

    files = []

    files_queue = Queue()
    if not object_ids:
        thread_files = Process(target=get_files, args=(path, files_queue))
        thread_files.start()
    else:
        thread_verif = Process(target=verif, args=(path, object_ids, files_queue))
        thread_verif.start()

    if render:
        render_queue = Queue()
        thread_render = Process(target=render_json, args=(schema, files_queue, render_queue))
        thread_render.start()

        return render_queue.get()

    return files


def verif(path, object_ids, files_queue):
    import os.path
    for (index, object_id) in enumerate(object_ids):
        s = get_file_by_id(path, object_id)
        if os.path.isfile(s):
            files_queue.put(s)
    files_queue.put(None)


def get_file_by_id(path, object_id):
    return path + "/" + str(object_id) + ".json"


def get_files(path, files_queue):
    import os
    [files_queue.put(path + "/" + file_name) for file_name in os.listdir(path)]
    files_queue.put(None)


def render_json(schema, files_queue, render_queue):
    from src.main.fsp.json_loader import json_loader
    json = "["
    loader = json_loader.load if schema is None else json_loader.load_with_schema
    file = files_queue.get()
    while file is not None:
        json += loader(path=file, schema=schema) + ","
        file = files_queue.get()
    if len(json) > 1:
        json = json[:-1]
    json += "]"
    render_queue.put(json)
