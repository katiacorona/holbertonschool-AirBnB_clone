#!/usr/bin/python3
"""
More tests... Review
"""

import unittest
import models
from models.base_model import BaseModel
from models.review import Review


class test_Review(unittest.TestCase):
    """
    Test cases for Review
    """

    def setUp(self):
        """
        Basic tests set up, create one example
        for the test
        """
        self.example = Review()

    def tearDown(self):
        """
        Erase examples used for tests
        """
        del self.example


if __name__ == '__main__':
    unittest.main()
