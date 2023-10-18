#!/usr/bin/python3
"""
Unittest for Place class.
"""
import unittest
import os
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """
    This class for testing the Place class.
    """
    def testPlaceCityID(self):
        s = Place()
        self.assertIn('city_id', dir(s))

    def testPlaceUserID(self):
        s = Place()
        self.assertIn('user_id', dir(s))

    def testPlaceName(self):
        s = Place()
        self.assertIn('name', dir(s))

    def testPlaceDescription(self):
        s = Place()
        self.assertIn('description', dir(s))

    def testPlaceNumberRooms(self):
        s = Place()
        self.assertIn('number_rooms', dir(s))

    def testPlaceNumberBathrooms(self):
        s = Place()
        self.assertIn('number_bathrooms', dir(s))

    def testPlaceMaxGuest(self):
        s = Place()
        self.assertIn('max_guest', dir(s))

    def testPlacePriceByNight(self):
        s = Place()
        self.assertIn('price_by_night', dir(s))

    def testPlaceLatitude(self):
        s = Place()
        self.assertIn('latitude', dir(s))

    def testPlaceLongitude(self):
        s = Place()
        self.assertIn('longitude', dir(s))

    def testPlaceAmenityIDs(self):
        s = Place()
        self.assertIn('amenity_ids', dir(s))
