#!/usr/bin/env python3
"""Test file for utility.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Utility testing class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """testing test_access_nested_map()"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """testing test_access_nested_map() for exceptions"""
        with self.assertRaises(KeyError) as message:
            access_nested_map(nested_map, path)
        self.assertEqual(str(message.exception), path[-1])


if __name__ == '__main__':
    unittest.main()
