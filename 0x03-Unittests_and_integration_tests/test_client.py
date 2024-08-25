#!/usr/bin/env python3
"""A module for testing the client module with and patch decorators."""

import unittest
from typing import Dict
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json", return_value={"key": "value"})
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Tests the org method of GithubOrgClient."""
        mocked_fxn.return_value = resp
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        url = f"https://api.github.com/orgs/{org}"
        mocked_fxn.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
