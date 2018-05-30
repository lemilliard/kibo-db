import os
import shutil

from src.admin.model.table import Table
from src.admin.model.descriptor.table_descriptor import TableDescriptor


class TableUtils(object):

    @staticmethod
    def get_table_descriptor(_db_system_name: str, _tb_system_name: str) -> TableDescriptor or bool:
        if not TableUtils.table_exists(_db_system_name, _tb_system_name):
            return False
        _file_path = files_directory + "/" + _db_system_name + "/" + _tb_system_name + "/" + _tb_system_name + ".json"
        return TableDescriptor.from_file(file_path=_file_path)

    @staticmethod
    def get_tables_descriptor(_db_system_name: str) -> list:
        _descriptors = []
        for _dir_name in TableUtils.get_table_dir_names(_db_system_name):
            _file_path = files_directory + "/" + _db_system_name + "/" + _dir_name + "/" + _dir_name + ".json"
            _descriptor = TableDescriptor.from_file(file_path=_file_path)
            _descriptors.append(_descriptor)
        return _descriptors

    @staticmethod
    def get_tables(_db_system_name: str) -> list:
        _tables = []
        _descriptors = TableUtils.get_tables_descriptor(_db_system_name)
        for _descriptor in _descriptors:
            _table = Table(
                db_system_name=_db_system_name,
                descriptor=_descriptor
            )
            _tables.append(_table)
        return _tables

    @staticmethod
    def get_table_dir_names(_db_system_name: str) -> list:
        dir_names = []
        if os.path.isdir(files_directory + "/" + _db_system_name):
            files = os.listdir(files_directory + "/" + _db_system_name)
            for file in files:
                if os.path.isdir(os.path.join(os.path.abspath(files_directory + "/" + _db_system_name), file)):
                    dir_names.append(file)
        return dir_names

    @staticmethod
    def create_table(_db_system_name: str, _name: str, _description: str) -> TableDescriptor or bool:
        _table = Table(
            db_system_name=_db_system_name,
            name=_name,
            description=_description
        )
        if TableUtils.table_exists(_db_system_name, _table.get_descriptor().get_system_name()):
            return False
        _table.to_file()
        return _table.get_descriptor()

    @staticmethod
    def delete_table(_db_system_name: str, _tb_system_name: str):
        if not TableUtils.table_exists(_db_system_name, _tb_system_name):
            return False
        shutil.rmtree(files_directory + "/" + _db_system_name + "/" + _tb_system_name)
        return True

    @staticmethod
    def table_exists(_db_system_name: str, _tb_system_name: str):
        _exists = False
        _tables = TableUtils.get_tables(_db_system_name)
        _i = 0
        while _i < len(_tables) and not _exists:
            if _tables[_i].get_descriptor().get_system_name() == _tb_system_name:
                _exists = True
            _i += 1
        return _exists
