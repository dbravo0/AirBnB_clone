#!/usr/bin/env python3
''' unit testing for Amenity class '''

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
        ''' class for testing Amenity '''

        def test_attribute_creation(self):
                ''' testing that instance initializes with correct
                attributes '''
                a = Amenity()
                self.assertEqual(type(a.name), str)
