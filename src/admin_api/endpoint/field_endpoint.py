from flask import request

from src.admin_api.model.field import Field
from src.admin_api.utils.cleaner_utils import CleanerUtils
from src.admin_api.utils.descriptor_utils import DescriptorUtils
from . import endpoint


class FieldEndpoint(endpoint.Endpoint):

    @staticmethod
    def process_request(_db_system_name: str, _tb_system_name: str, _fd_system_name: str = None):
        _response = "T'es con"
        if request.method == "GET":
            _response = FieldEndpoint.do_get(_db_system_name, _tb_system_name, _fd_system_name)
        elif request.method == "POST":
            _response = FieldEndpoint.do_post(_db_system_name, _tb_system_name)
        elif request.method == "PUT":
            _response = FieldEndpoint.do_put(_db_system_name, _tb_system_name, _fd_system_name)
        elif request.method == "DELETE":
            _response = FieldEndpoint.do_delete(_db_system_name, _tb_system_name, _fd_system_name)
        return _response

    @staticmethod
    def do_get(_db_system_name: str, _tb_system_name: str, _fd_system_name: str = None):
        _response = None
        _descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(_db_system_name, _tb_system_name)
        if _descriptor is not None:
            if _fd_system_name is None:
                _fields = []
                for _field in _descriptor.get_fields():
                    _fields.append(_field.to_dict())
                _response = _fields
            else:
                _field = _descriptor.get_field_by_system_name(_fd_system_name)
                if _field is not None:
                    _response = _field.to_dict()
        return _response

    @staticmethod
    def do_post(_db_system_name: str, _tb_system_name: str):
        _response = None
        _descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(_db_system_name, _tb_system_name)
        if _descriptor is not None:
            _body = FieldEndpoint.get_body()
            _name = _body.get("name", None)
            if _name is not None:
                _fd_system_name = CleanerUtils.generate_system_name(_name)
                if _descriptor.get_field_by_system_name(_fd_system_name) is None:
                    _id = _body.get("id", False)
                    _description = _body.get("description", None)
                    _type = _body.get("type", "string")
                    _field = Field(
                        id=_id,
                        name=_name,
                        description=_description,
                        type=_type
                    )
                    _descriptor.add_field(_field)
                    _descriptor.save(_db_system_name)
                    _response = _field.to_dict()
        return _response

    @staticmethod
    def do_put(_db_system_name: str, _tb_system_name: str, _fd_system_name: str):
        _response = None
        _descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(_db_system_name, _tb_system_name)
        if _descriptor is not None:
            _body = FieldEndpoint.get_body()
            if _fd_system_name is not None:
                _field = _descriptor.get_field_by_system_name(_fd_system_name)
                if _field is not None:
                    _id = _body.get("id", None)
                    if _id is not None:
                        _field.set_id(_id)
                    _name = _body.get("name", None)
                    if _name is not None:
                        _field.set_name(_name)
                    _description = _body.get("description", None)
                    if _description is not None:
                        _field.set_description(_description)
                    _type = _body.get("type", None)
                    if _type is not None:
                        _field.set_type(_type)
                    if _descriptor.update_field(_field):
                        _response = _field.to_dict()
                        _descriptor.save(_db_system_name)
        return _response

    @staticmethod
    def do_delete(_db_system_name: str, _tb_system_name: str, _fd_system_name: str):
        _response = None
        _descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(_db_system_name, _tb_system_name)
        if _descriptor is not None:
            _response = _descriptor.remove_field(_fd_system_name)
            _descriptor.save(_db_system_name)
        return _response
