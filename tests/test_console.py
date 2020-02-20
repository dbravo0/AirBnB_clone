#!/usr/bin/python3
"""Unit testing for AirBnB"""

import unittest
from unittest.mock import patch
import console
import json
import pep8
import os


class TestAirBnBConsole(unittest.TestCase):
    """Class for test the console"""

    def setUp(self):
        """Sets up test methods."""
        pass

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(console.HBNBCommand.__doc__)

if __name__ == '__main__':
    unittest.main()
