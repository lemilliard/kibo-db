from flask import request
from src.admin.utils import *


def endpoint(_dt_system_name, _tb_system_name):
    response = "T'es con"
    if request.method == 'GET':
        response = do_get(_dt_system_name, _tb_system_name)
    elif request.method == 'PUT':
        response = do_put(_dt_system_name, _tb_system_name)
    return response


def do_get(_db_system_name, _tb_system_name):
    return tb_descriptor.get_tb_descriptor(_db_system_name, _tb_system_name)


def do_put(_dt_system_name=None, _tb_system_name=None):
    response = None
    return response
