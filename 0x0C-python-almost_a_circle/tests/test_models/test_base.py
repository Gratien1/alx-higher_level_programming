#!/usr/bin/python3
"""
Tests for Base class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Base tests
    """


    def test_no_id(self):
        '''
            Sending no id
        '''
        b = Base()
        self.assertEqual(b.id, 1)
        
    def test_is_id(self):
        """
        id sent
        """
        b = Base(5)
        self.assertEqual(b.id, 5)
        
