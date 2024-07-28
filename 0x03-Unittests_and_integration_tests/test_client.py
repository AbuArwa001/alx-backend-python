#!/usr/bin/env python3
"""
Test module for GithubOrgClient
"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Implements the test_org method.
    """

    @parameterized.expand(
        [
            (
                "google",
                "https://api.github.com/orgs/google",
                {
                    "login": "google",
                    "url": "https://api.github.com/orgs/google",
                    "name": "Google",
                    "email": "opensource@google.com",
                    "type": "Organization",
                },
            ),
            (
                "abc",
                "https://api.github.com/orgs/abc",
                {
                    "login": "abc",
                    "url": "https://api.github.com/orgs/abc",
                    "name": "abc",
                    "email": "opensource@abc.com",
                    "type": "Organization",
                },
            ),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name, org_url, expected, mock_get_json):
        """
        This method should test that
        GithubOrgClient.org returns the correct value.
        """
        mock_get_json.return_value = expected
        test_git = GithubOrgClient(org_name)
        res = test_git.org
        mock_get_json.assert_called_once_with(org_url)
        self.assertEqual(res, expected)

    def test_public_repos_url(self):
        """
        Test return value for repos_url
        """
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "login": "abc",
                "repos_url": "https://api.github.com/orgs/abc/repos",
                "url": "https://api.github.com/orgs/abc",
                "name": "abc",
                "email": "opensource@abc.com",
                "type": "Organization",
            }
            org = GithubOrgClient("abc")
            res = org._public_repos_url
            self.assertEqual(res, "https://api.github.com/orgs/abc/repos")
