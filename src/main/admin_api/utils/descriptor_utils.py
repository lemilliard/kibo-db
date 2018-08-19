class DescriptorUtils(object):
    """Util class to work with descriptors

    Note:
        _system_name = file name
    """

    @staticmethod
    def get_dbs_descriptor() -> list:
        """Return list of databases descriptor"""
        _descriptors = []
        _db_dirs = DescriptorUtils.get_db_dirs()
        for _db_dir in _db_dirs:
            _descriptor = DescriptorUtils.get_db_descriptor_by_system_name(_db_dir)
            if _descriptor is not None:
                _descriptors.append(_descriptor)
        return _descriptors

    @staticmethod
    def get_db_descriptor_by_system_name(db_system_name: str):
        """Return database descriptor based on its dir"""
        import json
        from src.main.config import active_config
        from src.main.common.utils.file_utils import FileUtils
        from src.main.admin_api.model.database import Database

        descriptor = None
        if db_system_name is not None:
            json_file = db_system_name + ".json"
            db_path = FileUtils.join_path(active_config.files_directory, db_system_name)
            file_path = FileUtils.join_path(db_path, json_file)
            if FileUtils.does_file_exist(file_path):
                file = open(file_path)
                json_object = json.load(file)
                descriptor = Database.from_json(json_object)
                file.close()
        return descriptor

    @staticmethod
    def does_db_descriptor_exist(descriptor) -> bool:
        return DescriptorUtils.get_db_descriptor_by_system_name(descriptor.get_system_name()) is not None

    @staticmethod
    def get_tbs_descriptor(db_system_name: str) -> list:
        """Return list of tables descriptor of a database based on its database system name"""
        from src.main.config import active_config
        from src.main.common.utils.file_utils import FileUtils

        descriptors = []
        db_path = FileUtils.join_path(active_config.files_directory, db_system_name)
        for tb_dir in DescriptorUtils.get_tb_dirs(db_path):
            descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(db_system_name, tb_dir)
            if descriptor is not None:
                descriptors.append(descriptor)
        return descriptors

    @staticmethod
    def get_tb_descriptor_by_system_name(db_system_name: str, tb_system_name: str):
        """Return table descriptor based on its system name and its database system name"""
        import json
        from src.main.config import active_config
        from src.main.common.utils.file_utils import FileUtils
        from src.main.admin_api.model.table import Table

        descriptor = None
        if db_system_name is not None and tb_system_name is not None:
            json_file = tb_system_name + ".json"
            db_path = FileUtils.join_path(active_config.files_directory, db_system_name)
            tb_path = FileUtils.join_path(db_path, tb_system_name)
            file_path = FileUtils.join_path(tb_path, json_file)
            if FileUtils.does_file_exist(file_path):
                file = open(file_path)
                json_object = json.load(file)
                descriptor = Table.from_json(json_object)
                file.close()
        return descriptor

    @staticmethod
    def does_tb_descriptor_exist(db_system_name: str, descriptor) -> bool:
        return DescriptorUtils.get_tb_descriptor_by_system_name(
            db_system_name,
            descriptor.get_system_name()
        ) is not None

    @staticmethod
    def get_db_dirs() -> list:
        from src.main.config import active_config
        from src.main.common.utils.file_utils import FileUtils

        return FileUtils.get_sub_dirs(active_config.files_directory)

    @staticmethod
    def get_tb_dirs(_db_path: str) -> list:
        from src.main.common.utils.file_utils import FileUtils

        return FileUtils.get_sub_dirs(_db_path)
