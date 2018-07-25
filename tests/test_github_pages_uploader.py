#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `github_pages_uploader` package."""


import unittest
from click.testing import CliRunner

from github_pages_uploader import github_pages_uploader
from github_pages_uploader import cli


class TestGithub_pages_uploader(unittest.TestCase):
    """Tests for `github_pages_uploader` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'github_pages_uploader.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
