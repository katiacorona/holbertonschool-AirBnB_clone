#!/usr/bin/python3

import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_FileStorage(unittest.TestCase):
    """
    Tests for File_storage
    """

    def setUp(self):
        """
        Basic test sety up, create one example
        for the test
        """
        self.example = User()

    def tearDown(self):
        """
        When the test are over we use the tearDown
        to delete any object that we create
        """
        del self.example

    def test_new(self):
        """
        
        """

    def test_all(self):
        """
        
        """

    def test_save(self):
        """
        
        """

    def test_JSON(self):
        """
        """


if __name__ == "__main__":
    unittest.main()
