#!/usr/bin/python3
""" subclass defines a review """

from models.base_model import BaseModel


class Review(BaseModel):
    """subclass to define the Review and its attributes"""
    place_id = ""
    user_id = ""
    text = ""
