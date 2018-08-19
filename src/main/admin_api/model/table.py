from src.main.admin_api.model import descriptor


class Table(descriptor.Descriptor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = kwargs.get("fields", [])

    def get_fields(self):
        return self.fields

    def set_fields(self, fields):
        self.fields = fields

    def get_field_by_system_name(self, fd_system_name: str):
        field = None
        for f in self.fields:
            if f.get_system_name() == fd_system_name:
                field = f
        return field

    def add_field(self, _field):
        self.fields.append(_field)

    def remove_field(self, _fd_system_name: str) -> bool:
        _removed = False
        _field = self.get_field_by_system_name(_fd_system_name)
        if _field is not None:
            self.fields.remove(_field)
            _removed = True
        return _removed

    def update_field(self, field) -> bool:
        updated = False
        i = 0
        while i < len(self.fields) and not updated:
            if self.fields[i].get_system_name() == field.get_system_name():
                self.fields[i] = field
                updated = True
            i += 1
        return updated

    @staticmethod
    def from_json(_json: dict):
        from src.main.admin_api.model.field import Field

        name = _json.get("name", None)
        description = _json.get("description", None)
        system_name = _json.get("system_name", None)
        fields = _json.get("fields", [])
        f = []
        for field in fields:
            f.append(Field.from_json(field))
        return Table(
            name=name,
            description=description,
            system_name=system_name,
            fields=f
        )

    def to_dict(self, with_details: bool = False) -> dict:
        _object = super().to_dict()
        _object["fields"] = []
        for field in self.fields:
            _object["fields"].append(field.to_dict())
        return _object

    def save(self, db_system_name: str):
        import os
        import json
        from src.main.config import active_config

        if self.get_name() is not None and \
                self.get_system_name() is not None:
            dir_path = self.get_dir_path(db_system_name)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            data_path = self.get_data_dir_path(db_system_name)
            if not os.path.exists(data_path):
                os.makedirs(data_path)
            index_path = self.get_index_dir_path(db_system_name)
            if not os.path.exists(index_path):
                os.makedirs(index_path)
            file = open(self.get_file_path(db_system_name), "w")
            json.dump(self.to_dict(), file, indent=active_config.json_indent, separators=active_config.json_separators)
            file.close()
            for field in self.fields:
                field.save(db_system_name, self.system_name)

    def delete(self, db_system_name: str) -> bool:
        from src.main.common.utils.file_utils import FileUtils

        return FileUtils.delete_dir(self.get_dir_path(db_system_name))

    def get_dir_path(self, db_system_name: str) -> str:
        from src.main.config import active_config
        from src.main.common.utils.file_utils import FileUtils

        db_path = FileUtils.join_path(active_config.files_directory, db_system_name)
        return FileUtils.join_path(db_path, self.system_name)

    def get_data_dir_path(self, db_system_name: str) -> str:
        from src.main.config import active_config
        from src.main.common.utils.file_utils import FileUtils

        tb_path = self.get_dir_path(db_system_name)
        return FileUtils.join_path(tb_path, active_config.data_directory)

    def get_index_dir_path(self, db_system_name: str) -> str:
        from src.main.config import active_config
        from src.main.common.utils.file_utils import FileUtils

        tb_path = self.get_dir_path(db_system_name)
        return FileUtils.join_path(tb_path, active_config.index_directory)

    def get_file_path(self, _db_system_name: str) -> str:
        from src.main.common.utils.file_utils import FileUtils

        return FileUtils.join_path(self.get_dir_path(_db_system_name), self.system_name + ".json")
