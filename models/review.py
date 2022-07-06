#!/usr/bin/python3
"""
More classes that inherit from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    Public class attributes: place_id, user_id
    and name
    """

    place_id = ""
    user_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Calls for super() function to
        use the __init__ from BaseModel
        """
        super().__init__(*args, **kwargs)
