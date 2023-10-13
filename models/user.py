#!/usr/bin/python3
"""User's class, attributes and methods definitions"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """Defines the user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
