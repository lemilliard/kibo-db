from flask import request
from src.admin.utils import *
from src.admin.admin import get_body


def endpoint(_db_system_name):
    response = "T'es con"
    if request.method == "GET":
        response = do_get(_db_system_name)
    elif request.method == "POST":
        response = do_post(_db_system_name)
    return response


def do_get(_db_system_name):
    return tb_descriptor_utils.get_tbs_descriptor(_db_system_name)


def do_post(_db_system_name):
    _body = get_body()
    _name = _body["name"]
    _description = _body["description"]
    _db_descriptor = db_descriptor_utils.get_db_descriptor(_db_system_name)
    _db_descriptor['_tables'].append(_name)
    db_descriptor_utils.save_db_descriptor(_db_descriptor, _db_system_name)

