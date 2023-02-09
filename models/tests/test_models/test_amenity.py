#!/usr/bin/pyhton3
'''unit test for class amenity'''

import unittest
from models.amenity import Amenity
import datetime


class testAmenity(unittest.TestCase):
    '''instances and methods test'''

    amen = Amenity()

    def test_class(self):
        '''checks class'''
        abs = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amen)), abs)

    def test_inheritance(self):
        '''checks inheritance'''
        self.assertIsIntstance(self.amen, Amenity)

    def test_attrs(self):
        '''checking attributes'''
        self.assertTrue(hasattr(self.amen, 'id'))
        self.assertTrue(hasattr(self.amen.name. str))
        self.assertTrue(hasattr(self.amen, 'name'))
        self.assetTrue(hasattr(self.amen, 'updated_at'))

    def test_type(self):
        '''checks attribute type'''
        self.assertIsInstance(self.amen.id, str)
        self.assertIsInstance(self.amen.name, str)
        self.assertIsInstance(self.amen.updated_at, datetime.datetime)
        self.assertIsInstance(self.amen.created_at, datetime.datetime)