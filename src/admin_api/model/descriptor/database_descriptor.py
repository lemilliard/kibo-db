import os
import json

from src.config import Config
from . import descriptor


class DatabaseDescriptor(descriptor.Descriptor):

    @staticmethod
    def from_file(file_path: str):
        _json_object = json.load(open(file_path))
        _name = _json_object["_name"]
        _description = _json_object["_description"]
        _system_name = _json_object["_system_name"]
        return DatabaseDescriptor(
            name=_name,
            description=_description,
            system_name=_system_name
        )

    def save_file(self):
        _dir_path = self.get_dir_path()
        if not os.path.exists(_dir_path):
            os.makedirs(_dir_path)
        file = open(self.get_file_path(), "w")
        json.dump(self.__dict__, file, indent=Config.json_indent, separators=Config.json_separators)

    def get_dir_path(self):
        return Config.files_directory + "/" + self._system_name

    def get_file_path(self):
        return self.get_dir_path() + "/" + self._system_name + ".json"
