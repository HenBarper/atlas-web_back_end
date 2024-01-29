#!/usr/bin/env python3
"""Test file for client.py"""
import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
import fixtures


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

        mock_get_json.assert_called_once_with(github_client.ORG_URL.
                                              format(org=org_name))

    def test_public_repos_url(self):
        """testing for _public_repos_url()"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock)as mocked_obj:
            mocked_obj.return_value = {'repos_url': "https://testing.com"}
            myclass = GithubOrgClient('organization')
            self.assertEqual(myclass._public_repos_url, "https://testing.com")

    def test_public_repos(self):
        """testing for public_repos()"""
        pass

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "my_license")
    ])
    def test_has_license(self, license, user_license):
        """testing for has_licence()"""
        pass

@parameterized_class([
    fixtures.TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Client testing class for github org client"""
    def setUpClass(self):
        """set up class"""
        pass
    def tearDownClass(self):
        """teardown class"""
        pass

if __name__ == '__main__':
    unittest.main()
