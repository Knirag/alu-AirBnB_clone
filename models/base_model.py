#!usr/bin/python3
'''class basemodel that defines all common attributes/methods'''

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    '''parent class for all classes'''
    def __init__(self, *args, **kwargs):
        '''' Initializes attributes:date,uuid4'''
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs.__len__() > 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated-at':
                    value  = datetime.fromisoformat(value)
                    setattr(self, key, value)
                    continue
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        class_name = "[" + self.__class__.name__ +"]"
        1st = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(1st)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        date = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data