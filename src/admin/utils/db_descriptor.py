import os
import json

files_directory = '../databases'


def get_db_descriptor(_system_name):
    descriptor = None
    if does_db_folder_exists(_system_name):
        descriptor_file_path = files_directory + '/' + _system_name + '/' + _system_name + '.json'
        if os.path.isfile(descriptor_file_path):
            descriptor = json.load(open(descriptor_file_path))
    return descriptor


def get_dbs_descriptor():
    result = []
    for bdd_folder_name in get_dbs_folder_name():
        result.append(get_db_descriptor(bdd_folder_name))
    return result


def get_dbs_folder_name():
    files = os.listdir(files_directory)
    dirs = []
    for f in files:
        if os.path.isdir(os.path.join(os.path.abspath(files_directory), f)):
            dirs.append(f)
    return dirs


def does_db_folder_exists(_folder_name):
    exists = False
    bdd_folders_name = get_dbs_folder_name()
    i = 0
    while i < len(bdd_folders_name) and not exists:
        if bdd_folders_name[i] == _folder_name:
            exists = True
        i += 1
    return exists


def get_db_folder_files(_folder_name):
    return os.listdir(files_directory + '/' + _folder_name)


def get_tables_name(_db_system_name):
    _tables = []
    _db_descriptor = get_db_descriptor(_db_system_name)
    if _db_descriptor is not None:
        _tables = _db_descriptor['_tables']
    return _tables
