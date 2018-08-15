import json
from typing import List

from src.main.admin_api.model.database import Database
from src.main.admin_api.model.table import Table
from src.main.common.utils.file_utils import FileUtils
from src.main.config import Config


class DescriptorUtils(object):
    """Util class to work with descriptors

    Note:
        _system_name = file name
    """

    @staticmethod
    def get_dbs_descriptor() -> List[Database]:
        """Return list of databases descriptor"""
        _descriptors = []
        _db_dirs = DescriptorUtils.get_db_dirs()
        for _db_dir in _db_dirs:
            _descriptor = DescriptorUtils.get_db_descriptor_by_system_name(_db_dir)
            if _descriptor is not None:
                _descriptors.append(_descriptor)
        return _descriptors

    @staticmethod
    def get_db_descriptor_by_system_name(_db_system_name: str) -> Database or bool:
        """Return database descriptor based on its dir"""
        _descriptor = None
        if _db_system_name is not None:
            _json_file = _db_system_name + ".json"
            _db_path = FileUtils.join_path(Config.files_directory, _db_system_name)
            _file_path = FileUtils.join_path(_db_path, _json_file)
            if FileUtils.does_file_exist(_file_path):
                _file = open(_file_path)
                _json_object = json.load(_file)
                _descriptor = Database.from_json(_json_object)
                _file.close()
        return _descriptor

    @staticmethod
    def does_db_descriptor_exist(_descriptor: Database) -> bool:
        return DescriptorUtils.get_db_descriptor_by_system_name(_descriptor.get_system_name()) is not None

    @staticmethod
    def get_tbs_descriptor(_db_system_name: str) -> List[Table]:
        """Return list of tables descriptor of a database based on its database system name"""
        _descriptors = []
        _db_path = FileUtils.join_path(Config.files_directory, _db_system_name)
        for _tb_dir in DescriptorUtils.get_tb_dirs(_db_path):
            _descriptor = DescriptorUtils.get_tb_descriptor_by_system_name(_db_system_name, _tb_dir)
            if _descriptor is not None:
                _descriptors.append(_descriptor)
        return _descriptors

    @staticmethod
    def get_tb_descriptor_by_system_name(_db_system_name: str, _tb_system_name: str) -> Table or bool:
        """Return table descriptor based on its system name and its database system name"""
        _descriptor = None
        if _db_system_name is not None and _tb_system_name is not None:
            _json_file = _tb_system_name + ".json"
            _db_path = FileUtils.join_path(Config.files_directory, _db_system_name)
            _tb_path = FileUtils.join_path(_db_path, _tb_system_name)
            _file_path = FileUtils.join_path(_tb_path, _json_file)
            if FileUtils.does_file_exist(_file_path):
                _file = open(_file_path)
                _json_object = json.load(_file)
                _descriptor = Table.from_json(_json_object)
                _file.close()
        return _descriptor

    @staticmethod
    def does_tb_descriptor_exist(_db_system_name: str, _descriptor: Table) -> bool:
        return DescriptorUtils \
                   .get_tb_descriptor_by_system_name(_db_system_name, _descriptor.get_system_name()) is not None

    @staticmethod
    def get_db_dirs() -> List[str]:
        return FileUtils.get_sub_dirs(Config.files_directory)

    @staticmethod
    def get_tb_dirs(_db_path: str) -> List[str]:
        return FileUtils.get_sub_dirs(_db_path)
