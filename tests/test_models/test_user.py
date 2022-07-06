#!/usr/bin/python3
"""
More tests.... User
"""
import unittest
import models
from models.base_model import BaseModel
from models.user import User


class Test_User(unittest.TestCase):
    """
    Test cases for the User Class
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

    def test_init(self):
        """
        Test if an object of the class User can be created.
        without any parameters
        """
        new_obj = User()
        self.assertIsInstance(new_obj, User)

    def test_inheritance(self):
        """
        Test if an object of the class User can be created
        and inherits from BaseModel
        without any parameters
        """
        new_obj = User()
        self.assertIsInstance(new_obj, User)
        self.assertIsInstance(new_obj, BaseModel)

    def test_inheritance_parameters(self):
        """
        Test if an object of the class User have
        Id, created_at, updated_at
        """
        self.assertIsInstance(self.example, User)
        self.assertIsInstance(self.example, BaseModel)
        self.assertTrue(hasattr(self.example, "id"))
        self.assertTrue(hasattr(self.example, "created_at"))
        self.assertTrue(hasattr(self.example, "updated_at"))

    def test_user_first_name(self):
        """
        Test if an object of the class User can be created
        and then modify the parameters.
        Test for the First Name.
        """
        new_obj = User()
        new_obj.first_name = "Betty"
        new_obj.last_name = "Bar"
        new_obj.email = "airbnb@mail.com"
        new_obj.password = "root"
        self.assertIsInstance(new_obj, User)
        self.assertTrue(hasattr(new_obj, "first_name"))
        self.assertEqual(new_obj.first_name, "Betty")

    def test_user_last_name(self):
        """
        Test if an object of the class User can be created
        and then modify the parameters.
        Test for the Last Name.
        """
        new_obj = User()
        new_obj.first_name = "Betty"
        new_obj.last_name = "Bar"
        new_obj.email = "airbnb@mail.com"
        new_obj.password = "root"
        self.assertIsInstance(new_obj, User)
        self.assertTrue(hasattr(new_obj, "last_name"))
        self.assertEqual(new_obj.last_name, "Bar")

    def test_user_email(self):
        """
        Test if an object of the class User can be created
        and then modify the parameters.
        Test for the email.
        """
        new_obj = User()
        new_obj.first_name = "Betty"
        new_obj.last_name = "Bar"
        new_obj.email = "airbnb@mail.com"
        new_obj.password = "root"
        self.assertIsInstance(new_obj, User)
        self.assertTrue(hasattr(new_obj, "email"))
        self.assertEqual(new_obj.email, "airbnb@mail.com")

    def test_user_password(self):
        """
        Test if an object of the class User can be created
        and then modify the parameters.
        Test for the password.
        """
        new_obj = User()
        new_obj.first_name = "Betty"
        new_obj.last_name = "Bar"
        new_obj.email = "airbnb@mail.com"
        new_obj.password = "root"
        self.assertIsInstance(new_obj, User)
        self.assertTrue(hasattr(new_obj, "password"))
        self.assertEqual(new_obj.password, "root")

    def test_user_save(self):
        """
        Test if a user can be saved
        """
        new_obj = User()
        old_time = new_obj.updated_at
        new_obj.save()
        new_time = new_obj.updated_at
        self.assertNotEqual(old_time, new_time)

    def test_str(self):
        """
        Test if a user can use the __str__ method
        from the BaseModel class
        """
        test_id = self.example.id
        test_dic = self.example.__dict__
        str_to_cmp = "[User] ({}) {}".format(test_id, test_dic)
        self.assertEqual(str(self.example), str_to_cmp)

    def test_to_dict(self):
        """
        Test if User can use the to_dict method
        from the BaseModel class
        """
        new_obj = User()
        new_obj.first_name = "Betty"
        new_obj.last_name = "Bar"
        new_obj.email = "airbnb@mail.com"
        new_obj.password = "root"

        new_dict = new_obj.to_dict()

        self.assertIsInstance(new_dict['__class__'], str)
        self.assertIsInstance(new_dict['id'], str)
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)
        self.assertIsInstance(new_dict['first_name'], str)
        self.assertIsInstance(new_dict['last_name'], str)
        self.assertIsInstance(new_dict['email'], str)
        self.assertIsInstance(new_dict['password'], str)
