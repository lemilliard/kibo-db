import os
import json

from src.admin_api.utils.file_utils import FileUtils
from src.config import Config
from .descriptor import Descriptor


class Field(Descriptor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._id = kwargs.get("id", False)
        self._type = kwargs.get("type", "string")
        self._index = self._system_name

    def get_id(self) -> bool:
        return self._id

    def set_id(self, _id: bool):
        self._id = _id

    def get_type(self) -> bool:
        return self._type

    def set_type(self, _type: str):
        self._type = _type

    def get_index(self) -> bool:
        return self._index

    def set_index(self, _index: bool):
        self._index = _index

    def get_index_dir_path(self, _db_system_name: str, _tb_system_name: str) -> str:
        _db_path = FileUtils.join_path(Config.files_directory, _db_system_name)
        _tb_path = FileUtils.join_path(_db_path, _tb_system_name)
        _tb_index_path = FileUtils.join_path(_tb_path, Config.index_directory)
        return FileUtils.join_path(_tb_index_path, self._index + ".json")

    def save(self, _db_system_name: str, _tb_system_name: str):
        _index_file_path = self.get_index_dir_path(_db_system_name, _tb_system_name)
        if not os.path.exists(_index_file_path):
            file = open(_index_file_path, "w")
            json.dump([], file, indent=Config.json_indent, separators=Config.json_separators)
            file.close()

    @staticmethod
    def from_json_object(json_object: dict):
        _id = json_object["id"]
        _name = json_object["name"]
        _description = json_object["description"]
        _system_name = json_object["system_name"]
        _type = json_object["type"]
        _index = json_object["index"]
        return Field(
            id=_id,
            name=_name,
            description=_description,
            system_name=_system_name,
            type=_type,
            index=_index
        )

    def to_json_object(self):
        _json_object = dict()
        _json_object["id"] = self._id
        _json_object["name"] = self._name
        _json_object["description"] = self._description
        _json_object["system_name"] = self._system_name
        _json_object["type"] = self._type
        _json_object["index"] = self._index
        return _json_object
