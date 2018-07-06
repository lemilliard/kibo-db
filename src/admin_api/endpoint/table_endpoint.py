from flask import request

from . import endpoint
from src.admin_api.utils.table_utils import TableUtils


class TableEndpoint(endpoint.Endpoint):

    @staticmethod
    def process_request(_db_system_name: str, _tb_system_name: str = None):
        _response = "T'es con"
        if request.method == "GET":
            _response = TableEndpoint.do_get(_db_system_name, _tb_system_name)
        elif request.method == "POST":
            _response = TableEndpoint.do_post(_db_system_name)
        elif request.method == "PUT":
            _response = TableEndpoint.do_put(_db_system_name)
        elif request.method == "DELETE":
            _response = TableEndpoint.do_delete(_db_system_name, _tb_system_name)
        return _response

    @staticmethod
    def do_get(_db_system_name: str, _tb_system_name: str):
        _response = False
        if _tb_system_name is None:
            _descriptor_dicts = []
            _descriptors = TableUtils.get_tables_descriptor(_db_system_name)
            for _descriptor in _descriptors:
                _descriptor_dicts.append(_descriptor.__dict__)
                _response = _descriptor_dicts
        else:
            _descriptor = TableUtils.get_table_descriptor(_db_system_name, _tb_system_name)
            if _descriptor is not False:
                _response = _descriptor.__dict__
        return _response

    @staticmethod
    def do_post(_db_system_name):
        _response = False
        _body = TableEndpoint.get_body()
        _name = _body["name"]
        _description = _body["description"]
        _descriptor = TableUtils.create_table(_db_system_name, _name, _description)
        if _descriptor is not False:
            _response = _descriptor.__dict__
        return _response

    @staticmethod
    def do_put(_db_system_name: str):
        _response = False
        _body = TableEndpoint.get_body()
        _name = _body["name"]
        _description = _body["description"]
        _tb_system_name = _body["_system_name"]
        _descriptor = TableUtils.update_table(_db_system_name, _tb_system_name, _name, _description)
        if _descriptor is not False:
            _response = _descriptor.__dict__
        return _response

    @staticmethod
    def do_delete(_db_system_name: str, _tb_system_name: str):
        return TableUtils.delete_table(_db_system_name, _tb_system_name)
