import os
import shutil
from typing import List

from src.config import Config


class FileUtils(object):
    """Util class to work with files"""

    @staticmethod
    def get_sub_dirs(_dir: str) -> List[str]:
        """Return a list of directories in databases directory"""
        _dirs = []
        for _file in FileUtils.get_dir_files(_dir):
            if FileUtils.is_file_a_dir(_dir, _file):
                _dirs.append(_file)
        return _dirs

    @staticmethod
    def does_root_dir_exist() -> bool:
        return os.path.isdir(Config.files_directory)

    @staticmethod
    def get_dir_files(_dir: str) -> List[str]:
        if FileUtils.does_root_dir_exist():
            return os.listdir(_dir)
        return []

    @staticmethod
    def is_file_a_dir(_dir: str, _file: str):
        return os.path.isdir(FileUtils.join_path(_dir, _file))

    @staticmethod
    def join_path(_base_path: str, _path: str) -> str:
        return os.path.join(os.path.abspath(_base_path), _path)

    @staticmethod
    def does_file_exist(_file_path: str) -> bool:
        return os.path.exists(_file_path)

    @staticmethod
    def delete_dir(_dir: str) -> bool:
        _response = False
        if FileUtils.does_file_exist(_dir):
            shutil.rmtree(_dir)
            _response = True
        return _response
