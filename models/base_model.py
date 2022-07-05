#!/usr/bin/python3
"""
Defines the BaseModel class.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes/methods
    for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel.
        """
        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, dt_format)
                elif key != "__class__":
                    setattr(self, key, val)

    def save(self):
        """Updates the public instance attribute update_at."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance.

        Description: Includes key/value pairs for __class__, and converts
        created_at and updated_at to ISO.
        """
        f_dict = self.__dict__.copy()
        f_dict["__class__"] = self.__class__.__name__
        f_dict["created_at"] = self.created_at.isoformat()
        f_dict["updated_at"] = self.updated_at.isoformat()
        return f_dict

    def __str__(self):
        """Returns the print/str representation of BaseModel."""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
