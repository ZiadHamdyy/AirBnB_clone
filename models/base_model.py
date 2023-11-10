#!/usr/bin/python3
"""
"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        if (kwargs):
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())

            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
