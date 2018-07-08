from flask import request

from src.admin_api.model.table import Table
from src.admin_api.utils.descriptor_utils import DescriptorUtils
from . import endpoint


class TableEndpoint(endpoint.Endpoint):

    @staticmethod
    def process_request(_db_system_name: str, _tb_system_name: str = None):
        _response = "T'es con"
        if request.method == "GET":
            _response = TableEndpoint.do_get(_db_system_name, _tb_system_name)
        elif request.method == "POST":
            _response = TableEndpoint.do_post(_db_system_name)
        elif request.method == "PUT":
            _response = TableEndpoint.do_put(_db_system_name, _tb_system_name)
        elif request.method == "DELETE":
            _response = TableEndpoint.do_delete(_db_system_name, _tb_system_name)
        return _response

    @staticmethod
    def do_get(_db_system_name: str, _tb_system_name: str = None):
        _response = None
        if _tb_system_name is None:
            _descriptor_dicts = []
            _descriptors = DescriptorUtils.get_tbs_descriptor(_db_system_name)
            for _descriptor in _descriptors:
                _descriptor_dicts.append(_descriptor.to_json_object())
            _response = _descriptor_dicts
        else:
            _descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(_db_system_name, _tb_system_name)
            if _descriptor is not None:
                _response = _descriptor.to_json_object(True)
        return _response

    @staticmethod
    def do_post(_db_system_name):
        _response = None
        _body = TableEndpoint.get_body()
        _name = _body.get("name", None)
        if _name is not None:
            _description = _body.get("description", None)
            _fields = _body.get("fields", [])
            _descriptor = Table(name=_name, description=_description, fields=_fields)
            if not DescriptorUtils.does_tb_descriptor_exist(_db_system_name, _descriptor):
                _descriptor.save(_db_system_name)
                _response = _descriptor.to_json_object(True)
        return _response

    @staticmethod
    def do_put(_db_system_name: str, _tb_system_name: str):
        _response = None
        _body = TableEndpoint.get_body()
        if _tb_system_name is not None:
            _descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(_db_system_name, _tb_system_name)
            if _descriptor is not None:
                _name = _body.get("name", None)
                if _name is not None:
                    _descriptor.set_name(_name)
                _description = _body.get("description", None)
                if _description is not None:
                    _descriptor.set_description(_description)
                _fields = _body.get("fields", None)
                if _fields is not None:
                    _descriptor.set_fields(_fields)
                _descriptor.save(_db_system_name)
                _response = _descriptor.to_json_object(True)
        return _response

    @staticmethod
    def do_delete(_db_system_name: str, _tb_system_name: str):
        _response = None
        _descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(_db_system_name, _tb_system_name)
        if _descriptor is not None:
            _response = _descriptor.delete(_db_system_name)
        return _response
