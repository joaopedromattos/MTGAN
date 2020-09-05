#!/usr/bin/env python

"""Tests for `magic_card_generator` package."""


import unittest
from click.testing import CliRunner

from magic_card_generator import magic_card_generator
from magic_card_generator import cli


class TestMagic_card_generator(unittest.TestCase):
    """Tests for `magic_card_generator` package."""

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
        assert 'magic_card_generator.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
