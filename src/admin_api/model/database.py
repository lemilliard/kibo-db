import os
import json
from typing import List

from src.config import Config
from src.admin_api.utils.file_utils import FileUtils
from src.admin_api.utils import descriptor_utils

from .table import Table
from .descriptor import Descriptor


class Database(Descriptor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._tables: List[Table] = kwargs.get("tables", [])

    @staticmethod
    def from_file(_file_path: str):
        _json_object = json.load(open(_file_path))
        _name = _json_object["name"]
        _description = _json_object["description"]
        _system_name = _json_object["system_name"]
        return Database(
            name=_name,
            description=_description,
            system_name=_system_name
        )

    def save(self):
        _dir_path = self.get_dir_path()
        if not os.path.exists(_dir_path):
            os.makedirs(_dir_path)
        file = open(self.get_file_path(), "w")
        json.dump(self.to_dict(), file, indent=Config.json_indent, separators=Config.json_separators)
        file.close()

    def delete(self) -> bool:
        return FileUtils.delete_dir(self.get_dir_path())

    def get_dir_path(self) -> str:
        return FileUtils.join_path(Config.files_directory, self._system_name)

    def get_file_path(self) -> str:
        return FileUtils.join_path(self.get_dir_path(), self._system_name + ".json")

    def to_dict(self) -> dict:
        _object = super().to_dict()
        return _object

    def to_json_object(self, _with_tables: bool = False) -> dict:
        _json_object = super().to_dict()
        if _with_tables:
            _json_object["tables"] = []
            _tables = descriptor_utils.DescriptorUtils.get_tbs_descriptor(self.get_system_name())
            for _table in _tables:
                _json_object["tables"].append(_table.to_json_object())
        return _json_object
