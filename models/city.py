#!/usr/bin/python3
"""
More classes that inherit from BaseModel
"""

import models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel
    Public class attributes: state_id, name
    """

    state_id = ""
    name = ""
