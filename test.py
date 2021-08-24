#
# File: test.py
# Description: Runs the unit tests for this project
# Author: Bryan Peabody
#
import unittest
from Utils import dbUtils


class test_db_utils(unittest.TestCase):

    def test_get_full_url(self):
        result = dbUtils.get_full_url('http://127.0.0.1:4000/dnvAXnJaBA')
        expected = 'http://www.bryanpeabody.com'
        self.assertEqual(result, expected)

    def test_does_url_exist(self):
        result = dbUtils.does_full_url_exist('http://www.bryanpeabody.com')
        self.assertTrue(result)

    def test_add_new_url_pair(self):
        result = dbUtils.add_url_pair('test', 'test')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
