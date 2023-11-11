#!/usr/bin/python3
"""
Class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""

    state_id: str = ""
    name: str = ""
