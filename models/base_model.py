#!/usr/bin/python3
"""Base model"""

import models
import uuid
from datetime import datetime
import copy


class BaseModel:
    """
    Define attributes and methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        instances of the class:
             kwargs: args builder of BaseModel
             id, created_at, updated_at
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String of class name, id and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """
        String representation
        """
        return self.__str__()

    def save(self):
        """
        Update the public instance updated_at to the current one
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Create the class dictionary
        returns dictionary of all key values ​​in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["id"] = self.id
        return my_dict
