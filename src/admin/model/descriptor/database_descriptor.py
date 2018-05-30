import os
import json

from src.main import files_directory
from src.admin.utils.cleaner_utils import generate_system_name


class DatabaseDescriptor(object):

    def __init__(self, *args, **kwargs):
        self._name = kwargs.get("name")
        self._description = kwargs.get("description")
        self._system_name = kwargs.get("system_name", generate_system_name(self._name))

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_system_name(self):
        return self._system_name

    @staticmethod
    def from_file(file_path: str):
        json_object = json.load(open(file_path))
        _name = json_object["_name"]
        _description = json_object["_description"]
        _system_name = json_object["_system_name"]
        return DatabaseDescriptor(name=_name, description=_description, system_name=_system_name)

    def to_file(self):
        os.makedirs(self.get_dir_path())
        file = open(self.get_file_path(), "w")
        json.dump(self.__dict__, file)

    def get_dir_path(self):
        return files_directory + "/" + self._system_name

    def get_file_path(self):
        return self.get_dir_path() + "/" + self._system_name + ".json"
