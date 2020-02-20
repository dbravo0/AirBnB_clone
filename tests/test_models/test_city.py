#!/usr/bin/env python3
''' unit testing for City class '''

import unittest
import os
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
        ''' class for testing City '''

        def test_attribute_creation(self):
                ''' testing that instance initializes with correct
                attributes '''
                a = City()
                self.assertEqual(type(a.name), str)
                self.assertEqual(type(a.state_id), str)
