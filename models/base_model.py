#!/usr/bin/python3
''' This Modules is designed to define all attributes, intasces and functions for all other classes'''
import uuid
from datetime import datetime
import models


class BaseModel():
    ''' This class is base model for airBnB console project'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        '''string formating function'''
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
