import unittest
from unittest.mock import MagicMock

import os
import shutil

from src.main.common.utils.file_utils import FileUtils


class TestFileUtils(unittest.TestCase):

    def setUp(self):
        """Prépare les tests"""
        # Init mocked classes
        self.file_utils = FileUtils
        # Init constants
        self.dir_files = ['test1', 'test2']

    def test_get_sub_dirs_1(self):
        # Given
        self.file_utils.get_dir_files = MagicMock(return_value=self.dir_files)
        self.file_utils.is_file_a_dir = MagicMock(return_value=True)
        # When
        expected_value = self.dir_files
        returned_value = self.file_utils.get_sub_dirs('test')
        # Then
        self.assertListEqual(expected_value, returned_value)

    def test_get_sub_dirs_2(self):
        # Given
        dir_files = self.dir_files + ['test3']
        self.file_utils.get_dir_files = MagicMock(return_value=dir_files)
        is_file = [True, True, False]
        self.file_utils.is_file_a_dir = MagicMock(side_effect=is_file)
        # When
        expected_value = self.dir_files
        returned_value = self.file_utils.get_sub_dirs('test')
        # Then
        self.assertListEqual(expected_value, returned_value)

    def test_get_dir_files_1(self):
        # Given
        self.file_utils.does_root_dir_exist = MagicMock(return_value=True)
        os.listdir = MagicMock(return_value=self.dir_files)
        # When
        expected_value = self.dir_files
        returned_value = self.file_utils.get_dir_files('')
        # Then
        self.assertListEqual(expected_value, returned_value)

    def test_get_dir_files_2(self):
        # Given
        self.file_utils.does_root_dir_exist = MagicMock(return_value=False)
        # When
        expected_value = []
        returned_value = self.file_utils.get_dir_files('')
        # Then
        self.assertListEqual(expected_value, returned_value)

    def test_join_path(self):
        # Given
        base_path = 'D:/test1/'
        path = 'test2'
        # When
        expected_value = 'D:\\test1\\test2'
        returned_value = self.file_utils.join_path(base_path, path)
        # Then
        self.assertEqual(expected_value, returned_value)

    def test_delete_dir(self):
        # Given
        self.file_utils.does_file_exist = MagicMock(return_value=True)
        shutil.rmtree = MagicMock()
        # When
        expected_value = True
        returned_value = self.file_utils.delete_dir('./databases')
        # Then
        self.assertEqual(expected_value, returned_value)
