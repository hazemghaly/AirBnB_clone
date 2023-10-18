#!/usr/bin/python3
"""
Unittest for City class.
"""
import unittest
import os
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """
    This class for testing the City class.
    """

    def testCityName(self):
        s = City()
        self.assertIn('name', dir(s))

    def testCityStateID(self):
        s = City()
        self.assertIn('state_id', dir(s))
