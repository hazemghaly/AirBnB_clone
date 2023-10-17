#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """
    This class for testing a BaseModel class.
    """

    def testBaseModelSave(self):
        b = BaseModel()
        b.save()

    def testBaseModelToDict(self):
        b = BaseModel()
        my_dict = b.to_dict()

    def testBaseModelDifferentID(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def testBaseModelCreatedAt(self):
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime.datetime)

    def testBaseModelStr(self):
        b = BaseModel()
        self.assertIsInstance(b.__str__(), str)
