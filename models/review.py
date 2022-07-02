#!/usr/bin/python3
"""
More classes that inherit from BaseModel
"""

import models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    Public class attributes: place_id, user_id
    and name
    """

    place_id = ""
    user_id = ""
    name = ""
