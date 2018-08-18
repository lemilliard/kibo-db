class FileUtils(object):
    """Util class to work with files"""

    @staticmethod
    def get_sub_dirs(_dir: str) -> list:
        """Return a list of directories in databases directory"""
        dirs = []
        for file in FileUtils.get_dir_files(_dir):
            if FileUtils.is_file_a_dir(_dir, file):
                dirs.append(file)
        return dirs

    @staticmethod
    def does_root_dir_exist() -> bool:
        import os
        import src.main.config as config
        return os.path.isdir(config.Config.files_directory)

    @staticmethod
    def get_dir_files(_dir: str) -> list:
        import os
        if FileUtils.does_root_dir_exist():
            return os.listdir(_dir)
        return []

    @staticmethod
    def is_file_a_dir(_dir: str, file: str):
        import os
        return os.path.isdir(FileUtils.join_path(_dir, file))

    @staticmethod
    def join_path(base_path: str, path: str) -> str:
        import os
        return os.path.join(os.path.abspath(base_path), path)

    @staticmethod
    def does_file_exist(file_path: str) -> bool:
        import os
        return os.path.exists(file_path)

    @staticmethod
    def delete_dir(_dir: str) -> bool:
        import shutil
        response = False
        if FileUtils.does_file_exist(_dir):
            shutil.rmtree(_dir)
            response = True
        return response
