import os
import json
from typing import List

from src.config import Config
from src.admin_api.utils.file_utils import FileUtils

from .field import Field
from .descriptor import Descriptor


class Table(Descriptor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fields: List[Field] = kwargs.get("fields", [])

    def get_fields(self):
        return self._fields

    def set_fields(self, fields):
        self._fields = fields

    def get_field_by_system_name(self, _fd_system_name: str) -> Field:
        _field: Field = None
        for _f in self._fields:
            if _f.get_system_name() == _fd_system_name:
                _field = _f
        return _field

    def add_field(self, _field: Field):
        self._fields.append(_field)

    def remove_field(self, _fd_system_name: str) -> bool:
        _removed = False
        _field = self.get_field_by_system_name(_fd_system_name)
        if _field is not None:
            self._fields.remove(_field)
            _removed = True
        return _removed

    def update_field(self, _field: Field) -> bool:
        _updated = False
        _i = 0
        while _i < len(self._fields) and not _updated:
            if self._fields[_i].get_system_name() == _field.get_system_name():
                self._fields[_i] = _field
                _updated = True
            _i += 1
        return _updated

    @staticmethod
    def from_file(_file_path: str):
        json_object = json.load(open(_file_path))
        _name = json_object["name"]
        _description = json_object["description"]
        _system_name = json_object["system_name"]
        _fields = []
        for _field in json_object["fields"]:
            _fields.append(Field.from_json_object(_field))
        return Table(
            name=_name,
            description=_description,
            system_name=_system_name,
            fields=_fields
        )

    def save(self, _db_system_name: str):
        if self.get_name() is not None and \
                self.get_system_name() is not None:
            _dir_path = self.get_dir_path(_db_system_name)
            if not os.path.exists(_dir_path):
                os.makedirs(_dir_path)
            _data_path = self.get_data_dir_path(_db_system_name)
            if not os.path.exists(_data_path):
                os.makedirs(_data_path)
            _index_path = self.get_index_dir_path(_db_system_name)
            if not os.path.exists(_index_path):
                os.makedirs(_index_path)
            file = open(self.get_file_path(_db_system_name), "w")
            json.dump(self.to_dict(), file, indent=Config.json_indent, separators=Config.json_separators)
            file.close()
            for _field in self._fields:
                _field.save(_db_system_name, self._system_name)

    def delete(self, _db_system_name: str) -> bool:
        return FileUtils.delete_dir(self.get_dir_path(_db_system_name))

    def get_dir_path(self, _db_system_name: str) -> str:
        _db_path = FileUtils.join_path(Config.files_directory, _db_system_name)
        return FileUtils.join_path(_db_path, self._system_name)

    def get_data_dir_path(self, _db_system_name: str) -> str:
        _tb_path = self.get_dir_path(_db_system_name)
        return FileUtils.join_path(_tb_path, Config.data_directory)

    def get_index_dir_path(self, _db_system_name: str) -> str:
        _tb_path = self.get_dir_path(_db_system_name)
        return FileUtils.join_path(_tb_path, Config.index_directory)

    def get_file_path(self, _db_system_name: str) -> str:
        return FileUtils.join_path(self.get_dir_path(_db_system_name), self._system_name + ".json")

    def to_dict(self) -> dict:
        _json_object = super().to_dict()
        _json_object["fields"] = []
        for _field in self._fields:
            _json_object["fields"].append(_field.to_json_object())
        return _json_object

    def to_json_object(self, _with_fields: bool = False) -> dict:
        _json_object = super().to_dict()
        if _with_fields:
            _json_object["fields"] = []
            for _field in self._fields:
                _json_object["fields"].append(_field.to_json_object())
        return _json_object
