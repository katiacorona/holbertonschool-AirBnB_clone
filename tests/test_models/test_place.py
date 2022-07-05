#!/usr/bin/python3
"""
More tests... Place
"""

import unittest
import models
from models.base_model import BaseModel
from models.place import Place


class test_Place(unittest.TestCase):
    """
    Test cases for Place
    """

    def setUp(self):
        """
        Basic tests set up, create one example
        for the test
        """
        self.example = Place()

    def tearDown(self):
        """
        Erase examples used for tests
        """
        del self.example


if __name__ == "__main__":
    unittest.main()
