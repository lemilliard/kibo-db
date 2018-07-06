import os
import json

from src.config import Config
from . import descriptor


class TableDescriptor(descriptor.Descriptor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fields = kwargs.get("fields", [])

    def get_fields(self):
        return self._fields

    def set_fields(self, fields):
        self._fields = fields

    @staticmethod
    def from_file(_file_path: str):
        json_object = json.load(open(_file_path))
        _name = json_object["_name"]
        _description = json_object["_description"]
        _system_name = json_object["_system_name"]
        _fields = json_object["_fields"]
        return TableDescriptor(
            name=_name,
            description=_description,
            system_name=_system_name,
            fields=_fields
        )

    def save_file(self, _db_system_name: str):
        _dir_path = self.get_dir_path(_db_system_name)
        if not os.path.exists(_dir_path):
            os.makedirs(_dir_path)
        file = open(self.get_file_path(_db_system_name), "w")
        json.dump(self.__dict__, file, indent=Config.json_indent, separators=Config.json_separators)

    def get_dir_path(self, _db_system_name):
        return Config.files_directory + "/" + _db_system_name + "/" + self._system_name

    def get_file_path(self, _db_system_name):
        return self.get_dir_path(_db_system_name) + "/" + self._system_name + ".json"
