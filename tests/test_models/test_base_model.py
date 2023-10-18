#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""
import unittest
import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    This class for testing the BaseModel class.
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

    def testBaseModelCreateWithArgs(self):
        p1 = BaseModel([])
        self.assertIsInstance(p1, BaseModel)
        p2 = BaseModel({"id": "7b425ff5-00c1-4196-ba1b-542c7f7d068f",
                        "created_at": "2023-10-17T18:09:36.171374",
                        "updated_at": "2023-10-17T18:09:36.171376",
                        "__class__": "BaseModel"})
        self.assertEqual(
            p2.__str__(),
            "[{}] ({}) {}".format(
                p2.__class__.__name__,
                p2.id,
                p2.__dict__))
