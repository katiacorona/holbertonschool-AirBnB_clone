#!/usr/bin/python3
"""
Unittests for models/base_model.py.
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class Test_BaseModel_init(unittest.TestCase):
    """Unittests for instantiation of BaseModel class."""

    def test_no_args_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_dt(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_dt(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_id(self):
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)


class Test_BaseModel_save(unittest.TestCase):
    """Unittests for save method of BaseModel class."""

    def test_save_once(self):
        bm = BaseModel()
        sleep(0.03)
        bm.save()
        self.assertGreater(bm.updated_at, bm.created_at)

    def test_save_twice(self):
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
        bm = BaseModel()
        self.assertEqual(dict, type(bm.to_dict()))

    def test_to_dict_keys_exist(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())


if __name__ == '__main__':
    unittest.main()
