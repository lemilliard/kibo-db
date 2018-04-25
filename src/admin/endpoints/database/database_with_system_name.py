from flask import request
from src.admin.utils import *


def endpoint(_system_name):
    response = "T'es con"
    if request.method == 'GET':
        response = do_get(_system_name)
    elif request.method == 'PUT':
        response = do_put(_system_name)
    return response


def do_get(_system_name):
    response = None
    if _system_name is not None:
        response = db_descriptor.get_db_descriptor(_system_name)
    return response


def do_put(_system_name=None):
    response = None
    return response
