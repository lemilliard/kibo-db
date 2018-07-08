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

    @staticmethod
    def from_json(_json: dict):
        _name = _json.get("name", None)
        _description = _json.get("description", None)
        _system_name = _json.get("system_name", None)
        return Database(
            name=_name,
            description=_description,
            system_name=_system_name
        )

    def to_dict(self, _with_details: bool = False) -> dict:
        _dict = super().to_dict()
        _tables = descriptor_utils.DescriptorUtils.get_tbs_descriptor(self.get_system_name())
        _dict["tables"] = []
        if _with_details:
            for _table in _tables:
                _dict["tables"].append(_table.to_dict())
        return _dict
