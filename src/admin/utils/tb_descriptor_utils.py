import os
import json

from src.main import files_directory
from src.main import json_indent
from src.main import json_separators
from src.admin.utils.cleaner_utils import *


def get_tb_descriptor(_db_system_name, _tb_system_name):
    _descriptor = None
    _descriptor_file_path = files_directory + "/" + _db_system_name + "/" + _tb_system_name + "/" + _tb_system_name + ".json"
    if os.path.isfile(_descriptor_file_path):
        _descriptor = json.load(open(_descriptor_file_path))
    return _descriptor


def get_tbs_descriptor(_db_system_name):
    _tbs_descriptor = []
    for _tb_dir_name in get_tbs_dir_name(_db_system_name):
        _tbs_descriptor.append(get_tb_descriptor(_db_system_name, _tb_dir_name))
    return _tbs_descriptor


def get_tbs_dir_name(_db_system_name):
    _files = os.listdir(files_directory + "/" + _db_system_name)
    _dirs = []
    for _f in _files:
        if os.path.isdir(os.path.join(os.path.abspath(files_directory + "/" + _db_system_name), _f)):
            _dirs.append(_f)
    return _dirs


def does_tb_exist(_db_system_name, _tb_system_name):
    _exists = False
    _tbs_dir_name = get_tbs_dir_name(_db_system_name)
    _i = 0
    while _i < len(_tbs_dir_name) and not _exists:
        if _tbs_dir_name[_i] == _tb_system_name:
            _exists = True
        _i += 1
    return _exists


def create_tb_descriptor(_db_system_name, _name, _description):
    _tb_descriptor = generate_tb_descriptor(_name, _description)
    _tb_system_name = _tb_descriptor["_system_name"]
    if does_tb_exist(_tb_system_name):
        return False
    save_tb_descriptor(_tb_descriptor, _db_system_name, _tb_system_name)
    return _tb_descriptor


def generate_tb_descriptor(_name, _description, _system_name=None):
    _tb = dict()
    _clean_name = generate_clean_name(_name)
    _tb["_name"] = _clean_name
    _tb["_description"] = _description
    if _system_name is None:
        _tb["_system_name"] = generate_system_name(_clean_name)
    else:
        _tb["_system_name"] = _system_name
    _tb["_fields"] = []
    return _tb


def save_tb_descriptor(_tb_descriptor, _db_system_name, _tb_system_name):
    _tb_dir = files_directory + "/" + _db_system_name + "/" + _tb_system_name
    os.makedirs(_tb_dir)
    _tb_file = open(_tb_dir + "/" + _tb_system_name + ".json", "w")
    json.dump(_tb_descriptor, _tb_file, indent=json_indent, separators=json_separators)
