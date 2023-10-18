#!/usr/bin/python3
"""
Unittest for Review class.
"""
import unittest
import os
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    """
    This class for testing the Review class.
    """

    def testReviewPlaceID(self):
        s = Review()
        self.assertIn('place_id', dir(s))

    def testReviewUserID(self):
        s = Review()
        self.assertIn('user_id', dir(s))

    def testReviewText(self):
        s = Review()
        self.assertIn('text', dir(s))
