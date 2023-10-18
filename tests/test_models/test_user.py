#!/usr/bin/python3
"""
Unittest for User class.
"""
import unittest
import os
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """
    This class for testing the User class.
    """

    def testUserEmail(self):
        s = User()
        self.assertIn('email', dir(s))

    def testUserPassword(self):
        s = User()
        self.assertIn('password', dir(s))

    def testUserFirstName(self):
        s = User()
        self.assertIn('first_name', dir(s))

    def testUserLastName(self):
        s = User()
        self.assertIn('last_name', dir(s))
