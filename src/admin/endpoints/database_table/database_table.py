from flask import request
from src.admin.utils import *
from src.admin.admin import get_body


def endpoint(_db_system_name):
    response = "T'es con"
    if request.method == 'GET':
        response = do_get(_db_system_name)
    elif request.method == 'POST':
        response = do_post(_db_system_name)
    return response


def do_get(_db_system_name):
    return tb_descriptor.get_tbs_descriptor(_db_system_name)


def do_post(_db_system_name):
    response = None
    body = get_body()
    if body:
        response = body
    else:
        response = 'No body :o'
    return response
