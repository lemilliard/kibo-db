from flask import request

# from src.admin.admin import get_body
from src.admin.utils.table_utils import TableUtils


class TableEndpoint(object):

    @staticmethod
    def process_request(_db_system_name: str, _tb_system_name: str = None):
        response = "T'es con"
        if request.method == "GET":
            response = TableEndpoint.do_get(_db_system_name, _tb_system_name)
        elif request.method == "POST":
            response = TableEndpoint.do_post(_db_system_name)
        elif request.method == "PUT":
            _response = TableEndpoint.do_put(_db_system_name)
        elif request.method == "DELETE":
            _response = TableEndpoint.do_delete(_db_system_name, _tb_system_name)
        return response

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
            _response = TableUtils.get_table_descriptor(_db_system_name, _tb_system_name).__dict__
        return _response

    @staticmethod
    def do_post(_db_system_name):
        _body = TableEndpoint.get_body()
        _name = _body["name"]
        _description = _body["description"]
        # return tb_descriptor_utils.create_tb_descriptor(_db_system_name, _name, _description)

    @staticmethod
    def get_body():
        if request.json is None:
            return False
        return request.json
