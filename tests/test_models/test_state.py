#!/usr/bin/python3
"""
More tests... State
"""

import unittest
import models
from models.base_model import BaseModel
from models.state import State


class test_State(unittest.TestCase):
    """
    Test cases for State
    """

    def setUp(self):
        """
        Basic tests set up, create one example
        for the test
        """
        self.example = State()

    def tearDown(self):
        """
        Erase examples used for tests
        """
        del self.example

    def test_init(self):
        """
        Test if an object of the class State can be created.
        without any parameters
        """
        new_obj = State()
        self.assertIsInstance(new_obj, State)

    def test_inheritance(self):
        """
        Test if an object of the class State can be created
        and inherits from BaseModel
        without any parameters
        """
        new_obj = State()
        self.assertIsInstance(new_obj, State)
        self.assertIsInstance(new_obj, BaseModel)

    def test_inheritance_parameters(self):
        """
        Test if an object of the class State have
        Id, created_at, updated_at
        """
        self.assertIsInstance(self.example, State)
        self.assertIsInstance(self.example, BaseModel)
        self.assertTrue(hasattr(self.example, "id"))
        self.assertTrue(hasattr(self.example, "created_at"))
        self.assertTrue(hasattr(self.example, "updated_at"))

    def test_State_name(self):
        """
        Test if an object of the class State can be created
        and then modify the parameters.
        Test for the Name of the State.
        """
        new_obj = State()
        new_obj.name = "California"
        self.assertIsInstance(new_obj, State)
        self.assertTrue(hasattr(new_obj, "name"))
        self.assertEqual(new_obj.name, "California")

    def test_State_save(self):
        """
        Test if a State can be saved
        """
        new_obj = State()
        old_time = new_obj.updated_at
        new_obj.save()
        new_time = new_obj.updated_at
        self.assertNotEqual(old_time, new_time)

    def test_str(self):
        """
        Test if a State cls can use the __str__ method
        from the BaseModel class
        """
        test_id = self.example.id
        test_dic = self.example.__dict__
        str_to_cmp = "[State] ({}) {}".format(test_id, test_dic)
        self.assertEqual(str(self.example), str_to_cmp)

    def test_to_dict(self):
        """
        Test if State can use the to_dict method
        from the BaseModel class
        """
        new_obj = State()
        new_obj.name = "California"

        new_dict = new_obj.to_dict()

        self.assertIsInstance(new_dict['__class__'], str)
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)
        self.assertIsInstance(new_dict['name'], str)


if __name__ == '__main__':
    unittest.main()
