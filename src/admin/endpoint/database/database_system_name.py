import shutil
from flask import request

from src.main import files_directory
from src.admin.utils import *
from src.admin.admin import get_body
from src.admin.utils.database_utils import DatabaseUtils


def endpoint(_system_name):
    _response = "T'es con"
    if request.method == "GET":
        _response = do_get(_system_name)
    elif request.method == "PUT":
        _response = do_put(_system_name)
    elif request.method == "DELETE":
        _response = do_delete(_system_name)
    return _response


def do_get(_system_name):
    return DatabaseUtils.get_database_descriptor(_system_name).__dict__


def do_put(_system_name):
    _body = get_body()
    _name = _body["name"]
    _description = _body["description"]
    return db_descriptor_utils.update_db_descriptor(_name, _description, _system_name)


def do_delete(_system_name):
    return DatabaseUtils.delete_database(_system_name)


def delete_db(_system_name):
    if db_descriptor_utils.does_db_exist(_system_name):
        shutil.rmtree(files_directory + "/" + _system_name)
        return True
    return False
