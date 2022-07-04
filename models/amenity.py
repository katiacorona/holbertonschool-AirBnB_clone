#!/usr/bin/python3
"""
More classes that inherit from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amentiy class that inherits from BaseModel
    Public class attribute: name
    """

    name = ""
