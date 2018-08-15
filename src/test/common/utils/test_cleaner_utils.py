import unittest

from src.main.common.utils.cleaner_utils import CleanerUtils


class TestCleanerUtils(unittest.TestCase):

    def test_generate_clean_name(self):
        given_name = 'Test 01 àé  HELLO'
        expected_name = 'Test 01 ae HELLO'
        returned_name = CleanerUtils.generate_clean_name(given_name)
        self.assertEqual(expected_name, returned_name)

    def test_generate_system_name(self):
        given_name = 'Test 01 àé  HELLO'
        expected_name = 'test_01_àé__hello'
        returned_name = CleanerUtils.generate_system_name(given_name)
        self.assertEqual(expected_name, returned_name)

    def test_full_generate_system_name(self):
        given_name = 'Test 01 àé  HELLO'
        expected_name = 'test_01_ae_hello'
        clean_name = CleanerUtils.generate_clean_name(given_name)
        returned_name = CleanerUtils.generate_system_name(clean_name)
        self.assertEqual(expected_name, returned_name)
