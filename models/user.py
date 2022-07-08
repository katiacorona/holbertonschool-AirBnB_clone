#!/usr/bin/python3
"""
Firts user, class user inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User inherits from BaseModel and has the
    public attributes: email, password,
    first name and last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Calls for super() function to use the __init__ from parent __init__
        constructor (BaseModel).
        """
        super().__init__(*args, **kwargs)
