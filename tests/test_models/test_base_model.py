#!/usr/bin/python3
"""
Unittests for models/base_model.py.
"""
import models
import unittest
import pycodestyle
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Unittests pycodestyle for base_model."""

    def test_pycodestyle_check(self):
        """Checks if base_model passes pycodestyle."""
        style = pycodestyle.StyleGuide()
        checker = style.check_files(['models/base_model.py'])
        self.assertEqual(checker.total_errors, 0, "fix pycodestyle")

    def test_documentation_exists(self):
        """Checks that all classess and methods are documented."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_char_count_documentation(self):
        """Checks that documentation is at least 10 char long."""
        n = len(BaseModel.__doc__)
        self.assertGreaterEqual(n, 10)
        n = len(BaseModel.__init__.__doc__)
        self.assertGreaterEqual(n, 10)
        n = len(BaseModel.__str__.__doc__)
        self.assertGreaterEqual(n, 10)
        n = len(BaseModel.save.__doc__)
        self.assertGreaterEqual(n, 10)
        n = len(BaseModel.to_dict.__doc__)
        self.assertGreaterEqual(n, 10)


class Test_BaseModel_init(unittest.TestCase):
    """Unittests for instantiation of BaseModel class."""

    def test_no_args_instantiation(self):
        """Checks class for instantiation."""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        """Checks that assigned id is a public string."""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_dt(self):
        """Checks that created_at is a datetime public attribute."""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_dt(self):
        """Checks that updated_at is a datetime public attribute."""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_id(self):
        """Checks that every object gets a unique id."""
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_str_representation(self):
        """Checks string representation of the instance's dictionary."""
        bm = BaseModel()
        test_id = bm.id
        test_dict = bm.__dict__
        test_str = "[BaseModel] ({}) {}".format(test_id, test_dict)
        self.assertEqual(str(bm), test_str)


class Test_BaseModel_save(unittest.TestCase):
    """Unittests for save method of BaseModel class."""

    def test_save_once(self):
        """Checks that updated_at changes after running save method."""
        bm = BaseModel()
        sleep(0.03)
        bm.save()
        self.assertGreater(bm.updated_at, bm.created_at)

    def test_save_twice(self):
        """Checks that updated_at changes after running save method twice."""
        bm = BaseModel()
        sleep(0.03)
        checkpoint_1 = bm.updated_at
        bm.save()
        checkpoint_2 = bm.updated_at
        self.assertGreater(checkpoint_2, checkpoint_1)
        sleep(0.03)
        bm.save()
        self.assertGreater(bm.updated_at, checkpoint_2)


class Test_BaseModel_to_dict(unittest.TestCase):
    """Unittests for to_dict method of BaseModel class."""

    def test_to_dict_type(self):
        """Checks to_dict method returns a dictionary."""
        bm = BaseModel()
        self.assertEqual(dict, type(bm.to_dict()))

    def test_to_dict_keys_exist(self):
        """Checks that all keys are present in dictionary representation."""
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_added_attributes(self):
        """Checks that all added attributes are present in dict."""
        bm = BaseModel()
        bm.name = "Betty"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())


if __name__ == "__main__":
    unittest.main()
