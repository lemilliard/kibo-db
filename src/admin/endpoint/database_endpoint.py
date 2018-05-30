from flask import request

from src.admin.utils.database_utils import DatabaseUtils


class DatabaseEndpoint(object):

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
            _response = DatabaseUtils.get_database_descriptor(_db_system_name).__dict__
        return _response

    @staticmethod
    def do_post():
        _body = DatabaseEndpoint.get_body()
        _name = _body["name"]
        _description = _body["description"]
        _database = DatabaseUtils.create_database(_name, _description)
        if _database is not False:
            _database = _database.__dict__
        return _database

    @staticmethod
    def do_put():
        _body = DatabaseEndpoint.get_body()
        _name = _body["name"]
        _description = _body["description"]
        _system_name = _body["_system_name"]
        return True
        # return db_descriptor_utils.update_db_descriptor(_name, _description, _system_name)

    @staticmethod
    def do_delete(_db_system_name: str = None):
        return DatabaseUtils.delete_database(_db_system_name)

    @staticmethod
    def get_body():
        if request.json is None:
            return False
        return request.json
