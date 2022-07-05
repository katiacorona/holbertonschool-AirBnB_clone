#!/usr/bin/python3
"""
More classes that inherit from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel
    Public class attribute: name
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Calls for super() function to
        use the __init__ from BaseModel
        """
        super().__init__(*args, **kwargs)
