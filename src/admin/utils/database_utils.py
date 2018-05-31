import os
import shutil

from src.config import Config
from src.admin.model.database import Database
from src.admin.model.descriptor.database_descriptor import DatabaseDescriptor


class DatabaseUtils(object):

    @staticmethod
    def get_database_descriptor(_system_name: str) -> DatabaseDescriptor or bool:
        if not DatabaseUtils.database_exists(_system_name):
            return False
        _file_path = Config.files_directory + "/" + _system_name + "/" + _system_name + ".json"
        return DatabaseDescriptor.from_file(file_path=_file_path)

    @staticmethod
    def get_databases_descriptor() -> list:
        _descriptors = []
        for _dir_name in DatabaseUtils.get_database_dir_names():
            _file_path = Config.files_directory + "/" + _dir_name + "/" + _dir_name + ".json"
            _descriptor = DatabaseDescriptor.from_file(file_path=_file_path)
            _descriptors.append(_descriptor)
        return _descriptors

    @staticmethod
    def get_database(_system_name) -> Database or bool:
        if not DatabaseUtils.database_exists(_system_name):
            return False
        _file_path = Config.files_directory + "/" + _system_name + "/" + _system_name + ".json"
        return Database.from_file(_file_path)

    @staticmethod
    def get_databases() -> list:
        _databases = []
        _descriptors = DatabaseUtils.get_databases_descriptor()
        for _descriptor in _descriptors:
            _database = Database(descriptor=_descriptor)
            _databases.append(_database)
        return _databases

    @staticmethod
    def get_database_dir_names() -> list:
        dir_names = []
        if os.path.isdir(Config.files_directory):
            files = os.listdir(Config.files_directory)
            for file in files:
                if os.path.isdir(os.path.join(os.path.abspath(Config.files_directory), file)):
                    dir_names.append(file)
        return dir_names

    @staticmethod
    def create_database(name: str, description: str) -> DatabaseDescriptor or bool:
        _database = Database(name=name, description=description)
        if DatabaseUtils.database_exists(_database.get_descriptor().get_system_name()):
            return False
        _database.save_file()
        return _database.get_descriptor()

    @staticmethod
    def update_database(_db_system_name: str, _name: str,
                        _description: str) -> DatabaseDescriptor or bool:
        _response: DatabaseDescriptor or bool = False
        _descriptor: DatabaseDescriptor = DatabaseUtils.get_database_descriptor(_db_system_name)
        if _descriptor is not False:
            _descriptor.set_name(_name)
            _descriptor.set_description(_description)
            _descriptor.save_file()
            _response = _descriptor
        return _response

    @staticmethod
    def delete_database(_system_name: str) -> bool:
        if not DatabaseUtils.database_exists(_system_name):
            return False
        shutil.rmtree(Config.files_directory + "/" + _system_name)
        return True

    @staticmethod
    def database_exists(_system_name: str) -> bool:
        _exists: bool = False
        _databases: list = DatabaseUtils.get_databases()
        _i = 0
        while _i < len(_databases) and not _exists:
            if _databases[_i].get_descriptor().get_system_name() == _system_name:
                _exists = True
            _i += 1
        return _exists
