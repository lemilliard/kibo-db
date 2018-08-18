import os

import unittest
from unittest.mock import patch
from unittest.mock import MagicMock


class TestDatabase(unittest.TestCase):

    def setUp(self):
        from src.test.test_factory.descriptor_factory import DescriptorFactory

        self.database = DescriptorFactory.create_database()

    @patch("builtins.open")
    @patch("os.makedirs")
    @patch('json.dump')
    def test_save_1(self, m_open: MagicMock, m_os_makedirs: MagicMock, m_json_dump: MagicMock):
        # Given
        os.path.exists = MagicMock(return_value=True)
        self.database.get_dir_path = MagicMock(return_value="dir_path")
        self.database.get_file_path = MagicMock(return_value="file_path")
        self.database.to_dict = MagicMock(return_value=dict())
        # When
        self.database.save()
        # Then
        m_open.assert_called_once()
        m_os_makedirs.assert_not_called()
        m_json_dump.assert_called_once()

    @patch("builtins.open")
    @patch("os.makedirs")
    @patch('json.dump')
    def test_save_2(self, m_open: MagicMock, m_os_makedirs: MagicMock, m_json_dump: MagicMock):
        # Given
        os.path.exists = MagicMock(return_value=False)
        self.database.get_dir_path = MagicMock(return_value="dir_path")
        self.database.get_file_path = MagicMock(return_value="file_path")
        self.database.to_dict = MagicMock(return_value=dict())
        # When
        self.database.save()
        # Then
        m_open.assert_called_once()
        m_os_makedirs.assert_called_once()
        m_json_dump.assert_called_once()

    @patch("src.main.common.utils.file_utils.FileUtils.delete_dir")
    def test_delete(self, m_delete_dir):
        # Given
        self.database.get_dir_path = MagicMock(return_value="dir_path")
        # When
        self.database.delete()
        # Then
        m_delete_dir.assert_called_once()

    @patch("src.main.common.utils.file_utils.FileUtils.join_path")
    def test_get_dir_path(self, m_join_path):
        # Given
        # When
        self.database.get_dir_path()
        # Then
        m_join_path.assert_called_once()

    @patch("src.main.common.utils.file_utils.FileUtils.join_path")
    def test_get_file_path(self, m_join_path):
        # Given
        self.database.get_dir_path = MagicMock(return_value="dir_path")
        # When
        self.database.get_file_path()
        # Then
        self.database.get_dir_path.assert_called_once()
        m_join_path.assert_called_once()
