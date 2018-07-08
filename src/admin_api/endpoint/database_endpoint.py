from flask import request

from . import endpoint
from src.admin_api.utils.descriptor_utils import DescriptorUtils
from src.admin_api.model.database import Database


class DatabaseEndpoint(endpoint.Endpoint):

    @staticmethod
    def process_request(_db_system_name: str = None):
        _response = "T'es con"
        if request.method == "GET":
            _response = DatabaseEndpoint.do_get(_db_system_name)
        elif request.method == "POST":
            _response = DatabaseEndpoint.do_post()
        elif request.method == "PUT":
            _response = DatabaseEndpoint.do_put(_db_system_name)
        elif request.method == "DELETE":
            _response = DatabaseEndpoint.do_delete(_db_system_name)
        return _response

    @staticmethod
    def do_get(_db_system_name: str = None):
        _response = None
        if _db_system_name is None:
            _descriptor_dicts = []
            _descriptors = DescriptorUtils.get_dbs_descriptor()
            for _descriptor in _descriptors:
                _descriptor_dicts.append(_descriptor.to_json_object())
            _response = _descriptor_dicts
        else:
            _descriptor = DescriptorUtils.get_db_descriptor_by_system_name(_db_system_name)
            if _descriptor is not None:
                _response = _descriptor.to_json_object(True)
        return _response

    @staticmethod
    def do_post():
        _response = None
        _body = DatabaseEndpoint.get_body()
        _name = _body.get("name", None)
        if _name is not None:
            _description = _body.get("description", None)
            _descriptor = Database(name=_name, description=_description)
            if not DescriptorUtils.does_db_descriptor_exist(_descriptor):
                _descriptor.save()
                _response = _descriptor.to_json_object()
        return _response

    @staticmethod
    def do_put(_db_system_name: str):
        _response = None
        _body = DatabaseEndpoint.get_body()
        if _db_system_name is not None:
            _descriptor = DescriptorUtils.get_db_descriptor_by_system_name(_db_system_name)
            if _descriptor is not None:
                _name = _body.get("name", None)
                if _name is not None:
                    _descriptor.set_name(_name)
                _description = _body.get("description", None)
                if _description is not None:
                    _descriptor.set_description(_description)
                _descriptor.save()
                _response = _descriptor.to_json_object()
        return _response

    @staticmethod
    def do_delete(_system_name: str):
        _response = None
        _descriptor = DescriptorUtils.get_db_descriptor_by_system_name(_system_name)
        if _descriptor is not None:
            _response = _descriptor.delete()
        return _response
