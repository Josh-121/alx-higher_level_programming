#!/usr/bin/python3
"""
The Base class module
"""

import json


class Base:
    """
    Base class defination
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns input list of dictionaries in json string format
        """
        if not list_dictionaries:
            out = json.dumps([])
        else:
            out = json.dumps(list_dictionaries)
        return out

    @staticmethod
    def from_json_string(json_string):
        """
        coverts input json string to object and returns it
        """
        if not json_string:
            out = json.loads('[]')
        else:
            out = json.loads(json_string)
        return out

    @classmethod
    def save_to_file(cls, list_objs):
        """
        converts list of custom objects dictionary representation(gotten from
        input custom object list) to json string and saves it in a json file
        """
        if list_objs is not None:
            new_list = [i.to_dictionary() for i in list_objs]
            name = f"{str(cls.__name__)}.json"
            out = cls.to_json_string(new_list)
        else:
            out = '[]'
        with open(name, 'w') as file:
            file.write(out)

    @classmethod
    def create(cls, **dictionary):
        """
        creates and returns the respective class objects from the
        input specification
        """
        instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        returns a list of class objects gotten a json file
        containing their respective dict representations
        """
        name = f"{str(cls.__name__)}.json"
        with open(name, 'r') as file:
            out = file.read()
        out = cls.from_json_string(out)
        instance_list = [cls.create(**i) for i in out]
        return instance_list
