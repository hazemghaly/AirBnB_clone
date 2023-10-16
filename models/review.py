#!/usr/bin/python3
"""
This  classes that inherit from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    '''
class inherit from BaseModel.
'''
    place_id = ""
    user_id = ""
    text = ""
