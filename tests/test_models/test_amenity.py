#!/usr/bin/python3
"""
Unittest for Amenity class.
"""
import unittest
import os
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """
    This class for testing the Amenity class.
    """

    def testAmenityName(self):
        s = Amenity()
        self.assertIn('name', dir(s))
