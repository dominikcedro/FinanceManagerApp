"""
original author: Dominik Cedro
created: 2024-05-18
license: BSD 3.0
description: This module contains testing for database.py
"""

import unittest
from unittest.mock import patch, Mock
from sqlalchemy.exc import OperationalError

from source.database.database import setup_connection_db, query_all_prepare_with_analysis

class TestDatabase(unittest.TestCase):
    def setUp(self):
        Session = setup_connection_db()
        self.session = Session()

    def tearDown(self):
        self.session.close()

    @patch('source.database.database.create_engine')
    def test_setup_connection_db(self, mock_create_engine):
        mock_engine = Mock()
        mock_create_engine.return_value = mock_engine

        session = setup_connection_db()
        self.assertIsNotNone(session)

        mock_create_engine.assert_called_once()

    @patch('source.database.database.create_engine')
    def test_setup_connection_db_no_internet(self, mock_create_engine):
        mock_create_engine.side_effect = OperationalError(None, None, None)

        with self.assertRaises(OperationalError):
            setup_connection_db()

        mock_create_engine.assert_called_once()

if __name__ == '__main__':
    unittest.main()