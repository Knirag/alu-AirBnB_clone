#!/usr/bin/python3
"""Storage File(Serialization & Deserialization)"""

import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage:
    """This Serializes and Deserializes the Json file to Instances"""

__file_path = "file.json"
__objects = {}

def all(self):
    """returns the dict__objects"""
    return self._objects
def  new(self, obj):
    """Serialization"""
    key=obj.__class__.__name__+ '.' + obj.id