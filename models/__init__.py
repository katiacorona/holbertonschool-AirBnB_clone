#!/usr/bin/python3
"""
create a unique FileStorage instance for your application
"""

from models.engine import file_storage
from models.base_model import BaseModel

allclasses = {"BaseModel": BaseModel, "User": User,
              "State": State, "City": City, "Amenity": Amenity,
              "Place": Place, "Review": Review}
storage = file_storage.FileStorage()
storage.reload()
