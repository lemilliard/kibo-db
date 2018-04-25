from flask import request
from src.admin.utils import *
from src.admin.admin import get_body


def endpoint():
    response = "T'es con"
    if request.method == 'GET':
        response = do_get()
    elif request.method == 'POST':
        response = do_post()
    return response


def do_get():
    return db_descriptor.get_dbs_descriptor()


def do_post():
    response = None
    body = get_body()
    if body:
        response = body
    else:
        response = 'No body :o'
    return response
