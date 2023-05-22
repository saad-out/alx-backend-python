#!/usr/bin/env python3
"""
This module contains the unit tests for client.py
"""
from typing import List, Dict
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
import unittest

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class for testing GithubOrgClient
    """
    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('client.get_json')
    def test_org(
                 self,
                 org: str,
                 expected: Dict,
                 mocked_get_json: Mock
                 ) -> None:
        """
        Test that GithubOrgClient.org returns the correct value
        """
        mocked_get_json.return_value = expected
        org_client: GithubOrgClient = GithubOrgClient(org)
        self.assertEqual(org_client.org, expected)
        mocked_get_json.assert_called_once()

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mocked_org: Mock):
        """
        Test that the result of _public_repos_url is the expected one
        """
        payload = {
            "login": "google",
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        mocked_org.return_value = payload
        org_client: GithubOrgClient = GithubOrgClient("google")
        self.assertEqual(org_client._public_repos_url, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(
                          self,
                          mocked_get_json: Mock
                          ) -> None:
        """
        Test that the list of repos is what you expect from the chosen payload
        """
        REPOS_URL = "https://api.github.com/orgs/google/repos"
        repos = [
            {"id": 1, "name": "truth"},
            {"id": 2, "name": "autoparse"},
            {"id": 3, "name": "anvil-build"}
        ]
        mocked_get_json.return_value = repos
        with patch.object(
                          GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock
                          ) as mocked_repos_url:
            mocked_repos_url.return_value = REPOS_URL
            org_client: GithubOrgClient = GithubOrgClient("google")
            self.assertEqual(
                             org_client.public_repos(),
                             [repo["name"] for repo in repos]
                             )
            mocked_repos_url.assert_called_once()
        mocked_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
