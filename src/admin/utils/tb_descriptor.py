import os
import json

files_directory = '../databases'


def get_tb_descriptor(_db_system_name, _tb_system_name):
    descriptor = None
    descriptor_file_path = files_directory + '/' + _db_system_name + '/' + _tb_system_name + '/' + _tb_system_name + '.json'
    if os.path.isfile(descriptor_file_path):
        descriptor = json.load(open(descriptor_file_path))
    return descriptor


def get_tbs_descriptor(_db_system_name):
    result = []
    for bdd_folder_name in get_tbs_folder_name(_db_system_name):
        result.append(get_tb_descriptor(_db_system_name, bdd_folder_name))
    return result


def get_tbs_folder_name(_db_system_name):
    files = os.listdir(files_directory + '/' + _db_system_name)
    dirs = []
    for f in files:
        if os.path.isdir(os.path.join(os.path.abspath(files_directory + '/' + _db_system_name), f)):
            dirs.append(f)
    return dirs


def does_tb_folder_exists(_folder_name):
    exists = False
    tables_folder_name = get_tbs_folder_name()
    i = 0
    while i < len(tables_folder_name) and not exists:
        if tables_folder_name[i] == _folder_name:
            exists = True
        i += 1
    return exists
