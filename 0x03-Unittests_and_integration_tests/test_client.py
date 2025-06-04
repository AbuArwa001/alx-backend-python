#!/usr/bin/env python3
"""
Test module for GithubOrgClient
"""
import unittest
from unittest.mock import PropertyMock, patch

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class


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

    @patch(
        "client.get_json",
        return_value=[
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": None},
        ],
    )
    def test_public_repos(self, mock_get_json):
        """
        Unit-test GithubOrgClient.public_repos
        """
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_repos_url:
            mock_repos_url.return_value = (
                "https://api.github.com/orgs/abc/repos"
            )
            org = GithubOrgClient("abc")
            repos = org.public_repos()
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/abc/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test has license method
        """
        org = GithubOrgClient("abc")
        res = org.has_license(repo, license_key)
        self.assertEqual(res, expected)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for GithubOrgClient.public_repos
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the class for integration tests
        """
        cls.get_patcher = patch('requests.get',
                                side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the class for integration tests
        """
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """
        Mocked requests.get method to return appropriate payloads
        """
        class MockResponse:
            def __init__(self, json_data):
                self.json_data = json_data

            def json(self):
                return self.json_data

        if url == TEST_PAYLOAD[0][0]['repos_url']:
            return MockResponse(TEST_PAYLOAD[0][1])
        return MockResponse(TEST_PAYLOAD[0][0])

    def test_public_repos(self):
        """
        Test GithubOrgClient.public_repos method
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)

    def test_public_repos_with_license(self):
        """
        Test GithubOrgClient.public_repos method
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)
