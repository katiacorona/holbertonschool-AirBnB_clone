#!/usr/bin/python3
"""
Defines the BaseModel class.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """Initializes a new BaseModel.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Updates the public instance attribute update_at."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__."""
        pass

    def __str__(self):
        """Returns the print/str representation of BaseModel."""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
