#!/usr/bin/python3
"""Defines a base model class"""
import json


class Base:
    """Represent the base model
    Attributes:
        __nd_objects (int): The active number of Base instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base
        Args:
            id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts
        Args: list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None orlist_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
