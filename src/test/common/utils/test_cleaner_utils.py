import unittest


class TestCleanerUtils(unittest.TestCase):

    def setUp(self):
        from src.main.old.common.utils.cleaner_utils import CleanerUtils

        self.cleaner_utils = CleanerUtils

    def test_generate_clean_name(self):
        given_name = 'Test 01 àé  HELLO'
        expected_name = 'Test 01 ae HELLO'
        returned_name = self.cleaner_utils.generate_clean_name(given_name)
        self.assertEqual(expected_name, returned_name)

    def test_generate_system_name(self):
        given_name = 'Test 01 àé  HELLO'
        expected_name = 'test_01_àé__hello'
        returned_name = self.cleaner_utils.generate_system_name(given_name)
        self.assertEqual(expected_name, returned_name)

    def test_full_generate_system_name(self):
        given_name = 'Test 01 àé  HELLO'
        expected_name = 'test_01_ae_hello'
        clean_name = self.cleaner_utils.generate_clean_name(given_name)
        returned_name = self.cleaner_utils.generate_system_name(clean_name)
        self.assertEqual(expected_name, returned_name)
