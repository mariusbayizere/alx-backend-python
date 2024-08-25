#!/usr/bin/env python3
"""
Module to test the `GithubOrgClient` class and its methods.
"""

from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the `GithubOrgClient` class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """
        Test that `GithubOrgClient.org` returns the expected value.
        Mock the `get_json` method to ensure no external HTTP calls are made.
        """
        expected_payload = {"payload": True}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org()

        self.assertEqual(result, expected_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


if __name__ == "__main__":
    unittest.main()
