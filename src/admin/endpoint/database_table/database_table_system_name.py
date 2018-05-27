from flask import request
from src.admin.utils import *


def endpoint(_dt_system_name, _tb_system_name):
    _response = "T'es con"
    if request.method == "GET":
        _response = do_get(_dt_system_name, _tb_system_name)
    elif request.method == "PUT":
        _response = do_put(_dt_system_name, _tb_system_name)
    return _response


def do_get(_db_system_name, _tb_system_name):
    return tb_descriptor_utils.get_tb_descriptor(_db_system_name, _tb_system_name)


def do_put(_dt_system_name, _tb_system_name):
    response = None
    return response
