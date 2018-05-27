import os
import json

from src.main import files_directory
from src.main import json_indent
from src.main import json_separators
from src.admin.utils.cleaner_utils import *


def get_db_descriptor(_db_system_name):
    _db_descriptor = False
    if does_db_exist(_db_system_name):
        _db_descriptor_file = files_directory + "/" + _db_system_name + "/" + _db_system_name + ".json"
        if os.path.isfile(_db_descriptor_file):
            _db_descriptor = json.load(open(_db_descriptor_file))
    return _db_descriptor


def get_dbs_descriptor():
    _dbs_descriptor = []
    for _db_dir_name in get_dbs_dir_name():
        _dbs_descriptor.append(get_db_descriptor(_db_dir_name))
    return _dbs_descriptor


def get_dbs_dir_name():
    _dirs = []
    if os.path.isdir(files_directory):
        _files = os.listdir(files_directory)
        for _f in _files:
            if os.path.isdir(os.path.join(os.path.abspath(files_directory), _f)):
                _dirs.append(_f)
    return _dirs


def does_db_exist(_db_system_name):
    _exists = False
    _bdd_folders_name = get_dbs_dir_name()
    _i = 0
    while _i < len(_bdd_folders_name) and not _exists:
        if _bdd_folders_name[_i] == _db_system_name:
            _exists = True
        _i += 1
    return _exists


def get_tables_name(_db_system_name):
    _tables = []
    _db_descriptor = get_db_descriptor(_db_system_name)
    if _db_descriptor is not False:
        _tables = _db_descriptor["_tables"]
    return _tables


def create_db_descriptor(_name, _description):
    _db_descriptor = generate_db_descriptor(_name, _description)
    _db_system_name = _db_descriptor["_system_name"]
    if does_db_exist(_db_system_name):
        return False
    _db_dir = files_directory + "/" + _db_system_name
    os.makedirs(_db_dir)
    _db_file = open(_db_dir + "/" + _db_system_name + ".json", "w")
    json.dump(_db_descriptor, _db_file, indent=json_indent, separators=json_separators)
    return _db_descriptor


def update_db_descriptor(_name, _description, _system_name):
    _db_descriptor = get_db_descriptor(_system_name)
    _db_descriptor["_name"] = _name
    _db_descriptor["_description"] = _description
    save_db_descriptor(_db_descriptor, _system_name)
    return _db_descriptor


def save_db_descriptor(_db_descriptor, _system_name):
    _db_dir = files_directory + "/" + _system_name
    _db_file = open(_db_dir + "/" + _system_name + ".json", "w")
    json.dump(_db_descriptor, _db_file, indent=json_indent, separators=json_separators)


def generate_db_descriptor(_name, _description, _system_name=None):
    _db = dict()
    _clean_name = generate_clean_name(_name)
    _db["_name"] = _clean_name
    _db["_description"] = _description
    if _system_name is None:
        _db["_system_name"] = generate_system_name(_clean_name)
    else:
        _db["_system_name"] = _system_name
    _db["_tables"] = []
    return _db
