#!/usr/bin/env python3
"""Test file for client.py"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock

class TestGithubOrgClient(unittest.TestCase):
    """Client testing class for github org client"""
    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """testing org() method"""
        returned_payload = {}

        mock_response = Mock()
        mock_response.json.return_value = returned_payload

        mock_get_json.return_value = mock_response

        github_client = GithubOrgClient(org_name)
        github_client.org()

        mock_get_json.assert_called_once_with(github_client.ORG_URL.format(org=org_name))


if __name__ == '__main__':
    unittest.main()
