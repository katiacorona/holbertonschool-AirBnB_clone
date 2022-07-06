#!/usr/bin/python3
"""
More classes that inherit from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel
    Public class attributes: state_id, name
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Calls for super() function to
        use the __init__ from BaseModel
        """
        super().__init__(*args, **kwargs)
