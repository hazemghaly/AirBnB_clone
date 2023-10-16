#!/usr/bin/python3
"""
This module contains the BaseModel class.
"""
from models.base_model import BaseModel


class User (BaseModel):
    '''
class inherit from BaseModel.
'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
