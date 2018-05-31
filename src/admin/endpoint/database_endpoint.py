from flask import request

from . import endpoint
from src.admin.utils.database_utils import DatabaseUtils


class DatabaseEndpoint(endpoint.Endpoint):

    @staticmethod
    def process_request(_db_system_name: str = None):
        _response = "T'es con"
        if request.method == "GET":
            _response = DatabaseEndpoint.do_get(_db_system_name)
        elif request.method == "POST":
            _response = DatabaseEndpoint.do_post()
        elif request.method == "PUT":
            _response = DatabaseEndpoint.do_put()
        elif request.method == "DELETE":
            _response = DatabaseEndpoint.do_delete(_db_system_name)
        return _response

    @staticmethod
    def do_get(_db_system_name: str = None):
        _response = False
        if _db_system_name is None:
            _descriptor_dicts = []
            _descriptors = DatabaseUtils.get_databases_descriptor()
            for _descriptor in _descriptors:
                _descriptor_dicts.append(_descriptor.__dict__)
                _response = _descriptor_dicts
        else:
            _descriptor = DatabaseUtils.get_database_descriptor(_db_system_name)
            if _descriptor is not False:
                _response = _descriptor.__dict__
        return _response

    @staticmethod
    def do_post():
        _response = False
        _body = DatabaseEndpoint.get_body()
        _name = _body["name"]
        _description = _body["description"]
        _descriptor = DatabaseUtils.create_database(_name, _description)
        if _descriptor is not False:
            _response = _descriptor.__dict__
        return _response

    @staticmethod
    def do_put():
        _response = False
        _body = DatabaseEndpoint.get_body()
        _name = _body["name"]
        _description = _body["description"]
        _system_name = _body["_system_name"]
        _descriptor = DatabaseUtils.update_database(_system_name, _name, _description)
        if _descriptor is not False:
            _response = _descriptor.__dict__
        return _response

    @staticmethod
    def do_delete(_db_system_name: str):
        return DatabaseUtils.delete_database(_db_system_name)
