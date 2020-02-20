#!/usr/bin/env python3
''' unit testing for State class '''

import unittest
import os
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
        ''' class for testing State '''

        def test_attribute_creation(self):
                ''' testing that instance initializes with correct
                attributes '''
                a = State()
                self.assertEqual(type(a.name), str)
