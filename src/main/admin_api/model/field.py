from src.main.admin_api.model import descriptor


class Field(descriptor.Descriptor):

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

    def get_index_dir_path(self, db_system_name: str, tb_system_name: str) -> str:
        from src.main.config import active_config
        from src.main.common.utils.file_utils import FileUtils

        db_path = FileUtils.join_path(active_config.files_directory, db_system_name)
        tb_path = FileUtils.join_path(db_path, tb_system_name)
        tb_index_path = FileUtils.join_path(tb_path, active_config.index_directory)
        return FileUtils.join_path(tb_index_path, self.system_name + ".json")

    def save(self, db_system_name: str, tb_system_name: str):
        import os
        import json
        from src.main.config import active_config

        index_file_path = self.get_index_dir_path(db_system_name, tb_system_name)
        if not os.path.exists(index_file_path):
            file = open(index_file_path, "w")
            json.dump([], file, indent=active_config.json_indent, separators=active_config.json_separators)
            file.close()

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

    def to_dict(self, with_details: bool = False):
        _dict = super().to_dict()
        _dict["id"] = self._id
        _dict["type"] = self._type
        return _dict
