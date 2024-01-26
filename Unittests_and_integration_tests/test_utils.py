#!/usr/bin/env python3
"""Test file for utility.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Utility testing class"""
    # Example of syntax
    # def test_upper(self) -> str:
    #     """Test upper"""
    #     self.assertEqual('foo'.upper(), 'FOO')

    def test_1(self):
        """first sample test case: test_1()"""
        print("test one running")
        pass

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_param_1(self, nested_map, path, expected_output):
        """testing test_access_nested_map()"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)
        pass


if __name__ == '__main__':
    unittest.main()
