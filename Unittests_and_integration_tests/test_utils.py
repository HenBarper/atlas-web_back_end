#!/usr/bin/env python3
"""Test file for utility.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock
import requests


class TestAccessNestedMap(unittest.TestCase):
    """Utility testing class for access nested map"""
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
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Utility testing class for get json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, returned_payload):
        """testing getjson()"""
        mock_response = Mock()
        mock_response.json.return_value = returned_payload
        with patch('requests.get', return_value=mock_response):
            self.assertEqual(get_json(url), returned_payload)
            mock_response.json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
