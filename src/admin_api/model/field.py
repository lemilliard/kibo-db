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

    def get_id(self) -> bool:
        return self._id

    def set_id(self, _id: bool):
        self._id = _id

    def get_type(self) -> bool:
        return self._type

    def set_type(self, _type: str):
        self._type = _type

    def get_index_dir_path(self, _db_system_name: str, _tb_system_name: str) -> str:
        _db_path = FileUtils.join_path(Config.files_directory, _db_system_name)
        _tb_path = FileUtils.join_path(_db_path, _tb_system_name)
        _tb_index_path = FileUtils.join_path(_tb_path, Config.index_directory)
        return FileUtils.join_path(_tb_index_path, self._system_name + ".json")

    def save(self, _db_system_name: str, _tb_system_name: str):
        _index_file_path = self.get_index_dir_path(_db_system_name, _tb_system_name)
        if not os.path.exists(_index_file_path):
            _file = open(_index_file_path, "w")
            json.dump([], _file, indent=Config.json_indent, separators=Config.json_separators)
            _file.close()

    @staticmethod
    def from_json(_json: dict):
        _id = _json.get("id", False)
        _name = _json.get("name", None)
        _description = _json.get("description", None)
        _system_name = _json.get("system_name", None)
        _type = _json.get("type", "string")
        return Field(
            id=_id,
            name=_name,
            description=_description,
            system_name=_system_name,
            type=_type
        )

    def to_dict(self, _with_details: bool = False):
        _dict = super().to_dict()
        _dict["id"] = self._id
        _dict["type"] = self._type
        return _dict
