#!/usr/bin/python3
""" subclass defines a city """

from models.base_model import BaseModel


class City(BaseModel):
    """subclass to define the City and its attributes"""
    state_id = ""
    name = ""
