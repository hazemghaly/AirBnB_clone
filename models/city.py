#!/usr/bin/python3
"""
This  classes that inherit from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    '''
class inherit from BaseModel.
'''
    state_id = ""
    name = ""
