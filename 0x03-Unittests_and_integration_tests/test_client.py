#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class from the client module.
"""

from typing import Dict, Any
from parameterized import parameterized
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {"org": "google"}),
        ("abc", {"org": "abc"})
    ])
    @patch('client.get_json', return_value={"org": "google"})
    def test_org(self, org_name: str, expected_result: Dict[str, Any],
                 mock_get_json: Any) -> None:
        """
        Test that GithubOrgClient.org returns the correct value.

        Args:
            org_name (str): The name of the organization.
            expected_result (Dict[str, Any]): The expected result.
            mock_get_json (Any): The mock of the get_json function.
        """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), expected_result)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


if __name__ == "__main__":
    unittest.main()
