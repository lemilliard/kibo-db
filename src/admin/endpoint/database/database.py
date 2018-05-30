from flask import request

from src.admin.utils.database_utils import DatabaseUtils
from src.admin.admin import get_body


def endpoint():
    _response = "T'es con"
    if request.method == "GET":
        _response = do_get()
    elif request.method == "POST":
        _response = do_post()
    return _response


def do_get():
    _descriptor_dicts = []
    _descriptors = DatabaseUtils.get_databases_descriptor()
    for _descriptor in _descriptors:
        _descriptor_dicts.append(_descriptor.__dict__)
    return _descriptor_dicts


def do_post():
    _body = get_body()
    _name = _body["name"]
    _description = _body["description"]
    _database = DatabaseUtils.create_database(_name, _description)
    if _database is not False:
        _database = _database.__dict__
    return _database
