#!/usr/bin/env python3
"""
Test module for GithubOrgClient.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json', return_value={"key": "value"})
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        Ensure get_json is called with the correct URL.
        """
        client = GithubOrgClient(org_name)
        result = client.org()
        expected_url = f"https://api.github.com/orgs/{org_name}"
        
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, mock_get_json.return_value)


if __name__ == "__main__":
    unittest.main()
