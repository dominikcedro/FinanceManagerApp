"""
original author: Dominik Cedro
created: 2024-05-24
license: BSD 3.0
description: This module contains tests for the main.py
"""

import unittest
from unittest.mock import patch, MagicMock
from ..source import main

class TestMain(unittest.TestCase):

    @patch('main.argparse.ArgumentParser.parse_args')
    @patch('main.setup_connection_db')
    def test_add_op(self, mock_setup_connection_db, mock_parse_args):
        # Mock the command-line arguments
        mock_args = MagicMock()
        mock_args.command = 'add_op'
        mock_args.name_op = 'Test operation'
        mock_args.date = '2024-04-17 12:00:00'
        mock_args.op_type = 'expense'
        mock_args.category = 'Test category'
        mock_args.value = 100.0
        mock_parse_args.return_value = mock_args

        # Mock the database session
        mock_session = MagicMock()
        mock_setup_connection_db.return_value = mock_session

        # Mock the category query
        mock_category = MagicMock()
        mock_session.query().filter().first.return_value = mock_category

        # Run the main function
        main.main()

        # Check that a new operation was added to the session
        mock_session.add.assert_called_once()

        # Check that the session was committed
        mock_session.commit.assert_called_once()
