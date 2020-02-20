#!/usr/bin/env python3
''' unit testing for Review class '''

import unittest
import os
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
        ''' class for testing Review '''

        def test_attribute_creation(self):
                ''' testing that instance initializes with correct
                attributes '''
                a = Review()
                self.assertEqual(type(a.place_id), str)
                self.assertEqual(type(a.user_id), str)
                self.assertEqual(type(a.text), str)
