#!/usr/bin/python3
"""
Unittest for State class.
"""
import unittest
import os
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """
    This class for testing the State class.
    """

    def testStateName(self):
        s = State()
        self.assertIn('name', dir(s))
