#!/usr/bin/python3
"""
More classes that inherit from BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel
    Public class attributes: city_id, user_id,
    name, description, number_rooms, number_bathrooms,
    max_guest, price_of_night, latitude, logitude
    and amenity_ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Calls for super() function to
        use the __init__ from BaseModel
        """
        super().__init__(*args, **kwargs)
