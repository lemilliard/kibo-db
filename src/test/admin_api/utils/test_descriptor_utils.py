import unittest

from unittest.mock import MagicMock

from src.main.admin_api.model.table import Table
from src.main.admin_api.utils.descriptor_utils import DescriptorUtils


class DescriptorUtilsTest(unittest.TestCase):

    def setUp(self):
        self.table = Table(name='TableName', description='TableDescription')
        self.database_list = []

    def test_does_tb_descriptor_exist_1(self):
        descriptor_utils = DescriptorUtils
        descriptor_utils.get_tb_descriptor_by_system_name = MagicMock(return_value={})
        expected_value = True
        returned_value = descriptor_utils.does_tb_descriptor_exist('DatabaseName', self.table)
        self.assertEqual(expected_value, returned_value)

    def test_does_tb_descriptor_exist_2(self):
        descriptor_utils = DescriptorUtils
        descriptor_utils.get_tb_descriptor_by_system_name = MagicMock(return_value=None)
        expected_value = False
        returned_value = descriptor_utils.does_tb_descriptor_exist('DatabaseName', self.table)
        self.assertEqual(expected_value, returned_value)
