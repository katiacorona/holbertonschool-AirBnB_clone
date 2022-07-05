#!/usr/bin/python3
"""
More tests... Amenity
"""

import unittest
import models
from models.base_model import BaseModel
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """
    Test cases for Amenity
    """

    def setUp(self):
        """
        Basic tests set up, create one example
        for the test
        """
        self.example = Amenity()

    def tearDown(self):
        """
        Erase examples used for tests
        """
        del self.example

    def test_init(self):
        """
        Test if an object of the class amenity can be created.
        without any parameters
        """
        new_obj = Amenity()
        self.assertIsInstance(new_obj, Amenity)

    def test_inheritance(self):
        """
        Test if an object of the class Amenity can be created
        and inherits from BaseModel
        without any parameters
        """
        new_obj = Amenity()
        self.assertIsInstance(new_obj, Amenity)
        self.assertIsInstance(new_obj, BaseModel)

    def test_inheritance_parameters(self):
        """
        Test if an object of the class Amenity have
        Id, created_at, updated_at
        """
        self.assertIsInstance(self.example, Amenity)
        self.assertIsInstance(self.example, BaseModel)
        self.assertTrue(hasattr(self.example, "id"))
        self.assertTrue(hasattr(self.example, "created_at"))
        self.assertTrue(hasattr(self.example, "updated_at"))

    def test_Amenity_name(self):
        """
        Test if an object of the class Amenity can be created
        and then modify the parameters.
        Test for the Name of the Amenity.
        """
        new_obj = Amenity()
        new_obj.name = "Pool"
        self.assertIsInstance(new_obj, Amenity)
        self.assertTrue(hasattr(new_obj, "name"))
        self.assertEqual(new_obj.name, "Pool")

    def test_Amenity_save(self):
        """
        Test if an Amenity can be saved
        """
        new_obj = Amenity()
        old_time = new_obj.updated_at
        new_obj.save()
        new_time = new_obj.updated_at
        self.assertNotEqual(old_time, new_time)

    def test_str(self):
        """
        Test if an Amenity cls can use the __str__ method
        from the BaseModel class
        """
        test_id = self.example.id
        test_dic = self.example.__dict__
        str_to_cmp = "[Amenity] ({}) {}".format(test_id, test_dic)
        self.assertEqual(str(self.example), str_to_cmp)

    def test_to_dict(self):
        """
        Test if Amenity can use the to_dict method
        from the BaseModel class
        """
        new_obj = Amenity()
        new_obj.name = "Pool"

        new_dict = new_obj.to_dict()

        self.assertIsInstance(new_dict['__class__'], str)
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)
        self.assertIsInstance(new_dict['name'], str)


if __name__ == '__main__':
    unittest.main()
