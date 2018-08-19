from src.main.admin_api.model import descriptor


class Database(descriptor.Descriptor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._tables = kwargs.get("tables", [])

    def save(self):
        import os
        import json
        from src.main.config import active_config

        dir_path = self.get_dir_path()
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file = open(self.get_file_path(), "w")
        json.dump(self.to_dict(), file, indent=active_config.json_indent, separators=active_config.json_separators)
        file.close()

    def delete(self) -> bool:
        from src.main.common.utils.file_utils import FileUtils

        return FileUtils.delete_dir(self.get_dir_path())

    def get_dir_path(self) -> str:
        from src.main.config import active_config
        from src.main.common.utils.file_utils import FileUtils

        return FileUtils.join_path(active_config.files_directory, self.system_name)

    def get_file_path(self) -> str:
        from src.main.common.utils.file_utils import FileUtils

        return FileUtils.join_path(self.get_dir_path(), self.system_name + ".json")

    @staticmethod
    def from_json(_json: dict):
        name = _json.get("name", None)
        description = _json.get("description", None)
        system_name = _json.get("system_name", None)
        return Database(
            name=name,
            description=description,
            system_name=system_name
        )

    def to_dict(self, with_details: bool = False) -> dict:
        from src.main.admin_api.utils.descriptor_utils import DescriptorUtils

        _dict = super().to_dict()
        tables = DescriptorUtils.get_tbs_descriptor(self.get_system_name())
        if with_details:
            _dict["tables"] = []
            for table in tables:
                _dict["tables"].append(table.to_dict())
        return _dict
