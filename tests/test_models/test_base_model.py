#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""
import unittest
import datetime
from models.base_model import BaseModel
from models import storage


class TestBase(unittest.TestCase):
    """
    This class for testing a BaseModel class.
    """

    def testBaseModelSave(self):
        b = BaseModel()
        updated_time_1 = b.updated_at
        b.save()
        updated_time_2 = b.updated_at
        self.assertNotEqual(updated_time_1, updated_time_2)

    def testBaseModelToDict(self):
        b = BaseModel()
        my_dict = b.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertEqual(b.id, my_dict['id'])
        self.assertEqual(b.created_at.isoformat(), my_dict['created_at'])
        self.assertEqual(b.updated_at.isoformat(), my_dict['updated_at'])
        self.assertEqual(b.__class__.__name__, my_dict['__class__'])

    def testBaseModelDifferentID(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def testBaseModelCreatedAt(self):
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime.datetime)

    def testBaseModelStr(self):
        b = BaseModel()
        my_str = "[{}] ({}) {}".format(
                        b.__class__.__name__,
                        b.id,
                        b.__dict__)
        self.assertIsInstance(b.__str__(), str)
        self.assertEqual(b.__str__(), my_str)
