import os
import json

from src.admin.utils.cleaner_utils import generate_system_name


class TableDescriptor:

    def __init__(self, *args, **kwargs):
        self._name = kwargs.get("name")
        self._description = kwargs.get("description")
        self._system_name = kwargs.get("system_name", generate_system_name(self._name))
        self._fields = kwargs.get("fields", [])

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_system_name(self):
        return self._system_name

    def get_fields(self):
        return self._fields

    @staticmethod
    def from_file(file_path: str):
        json_object = json.load(open(file_path))
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

    def to_file(self, _db_system_name):
        os.makedirs(self.get_dir_path(_db_system_name))
        file = open(self.get_file_path(_db_system_name), "w")
        json.dump(self.__dict__, file)

    def get_dir_path(self, _db_system_name):
        return files_directory + "/" + _db_system_name + "/" + self._system_name

    def get_file_path(self, _db_system_name):
        return self.get_dir_path(_db_system_name) + "/" + self._system_name + ".json"
