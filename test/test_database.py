"""
original author: Dominik Cedro
created: 2024-05-18
license: BSD 3.0
description: This module contains testing for database.py
"""

import unittest
from unittest.mock import patch, Mock
from sqlalchemy.exc import OperationalError

from source.database.database import setup_connection_db, query_all_prepare_with_analysis, count_entries_in_db, \
    query_by_category, query_by_month


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

    # @patch('source.database.database.create_engine')
    # def test_setup_connection_db_no_internet(self, mock_create_engine):
    #     mock_create_engine.side_effect = OperationalError(None, None, None)
    #
    #     with self.assertRaises(OperationalError):
    #         setup_connection_db()
    #
    #     mock_create_engine.assert_called_once()
    #
    # @patch('source.database.database.sessionmaker')
    # @patch('source.database.database.FinOpModel')
    # def test_query_all_prepare_with_analysis(self, mock_finop_model, mock_sessionmaker):
    #     mock_session = Mock()
    #     mock_sessionmaker.return_value = mock_session
    #
    #     mock_query = Mock()
    #     mock_session.query.return_value = mock_query
    #
    #     mock_filter = Mock()
    #     mock_query.filter.return_value = mock_filter
    #
    #     mock_all = Mock()
    #     mock_all.all.return_value = []
    #     mock_filter.all.return_value = mock_all
    #
    #     analysis = query_all_prepare_with_analysis(mock_session)
    #     self.assertIsNotNone(analysis)
    #
    #     mock_session.query.assert_called_once_with(mock_finop_model)
    #     mock_filter.all.assert_called_once()

if __name__ == '__main__':
    unittest.main()