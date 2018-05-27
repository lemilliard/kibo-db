from flask import request

from src.admin.utils import *
from src.admin.admin import get_body
from src.admin.utils.cleaner_utils import *


def endpoint():
    _response = "T'es con"
    if request.method == "GET":
        _response = do_get()
    elif request.method == "POST":
        _response = do_post()
    return _response


def do_get():
    return db_descriptor_utils.get_dbs_descriptor()


def do_post():
    _body = get_body()
    _name = _body["name"]
    _description = _body["description"]
    return db_descriptor_utils.create_db_descriptor(_name, _description)
