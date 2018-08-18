import unittest
from unittest.mock import MagicMock


class TestDescriptorUtils(unittest.TestCase):

    def setUp(self):
        from src.main.admin_api.utils.descriptor_utils import DescriptorUtils
        from src.test.test_factory.descriptor_factory import DescriptorFactory

        """Prépare les tests"""
        # Init mocked classes
        self.descriptor_utils = DescriptorUtils
        # Init constants
        self.list_size = 10
        self.table = DescriptorFactory.create_table()
        self.database = DescriptorFactory.create_database()
        self.database_list = DescriptorFactory.create_database_list(self.list_size)
        self.database_name_list = DescriptorFactory.create_database_name_list(self.list_size)

    def test_get_dbs_descriptor(self):
        """Verifie que la méthode ne retourne pas de base sans descripteur"""
        # Given
        database_name_list = self.database_name_list + ['Test']
        self.descriptor_utils \
            .get_db_dirs = MagicMock(return_value=database_name_list)

        descriptors = self.database_list + [None]
        self.descriptor_utils \
            .get_db_descriptor_by_system_name = MagicMock(side_effect=descriptors)
        # When
        expected_value = self.database_list
        returned_value = self.descriptor_utils.get_dbs_descriptor()
        # Then
        self.descriptor_utils \
            .get_db_dirs.assert_called_once()
        get_descriptor_calls = self.descriptor_utils \
            .get_db_descriptor_by_system_name.call_count
        self.assertEqual(get_descriptor_calls, len(database_name_list))
        self.assertListEqual(expected_value, returned_value)

    def test_does_tb_descriptor_exist_1(self):
        """Vérifie que la méthode renvoie True quand la table existe"""
        from src.test.test_factory.descriptor_factory import DescriptorFactory

        # Given
        self.descriptor_utils \
            .get_tb_descriptor_by_system_name = MagicMock(return_value=self.table)
        # When
        expected_value = True
        returned_value = self.descriptor_utils \
            .does_tb_descriptor_exist(DescriptorFactory.database_name, self.table)
        # Then
        self.assertEqual(expected_value, returned_value)

    def test_does_tb_descriptor_exist_2(self):
        """Vérifie que la méthode renvoie False quand la table n'existe pas"""
        from src.test.test_factory.descriptor_factory import DescriptorFactory

        # Given
        self.descriptor_utils \
            .get_tb_descriptor_by_system_name = MagicMock(return_value=None)
        # When
        expected_value = False
        returned_value = self.descriptor_utils \
            .does_tb_descriptor_exist(DescriptorFactory.table_name, self.table)
        # Then
        self.assertEqual(expected_value, returned_value)
