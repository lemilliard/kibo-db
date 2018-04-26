import os
import json
from src.main import files_directory


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
