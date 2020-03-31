#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128),
                  nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            _cities = []
            for _id, city in models.storage.all(City).items():
                if self.id == city.state_id:
                    _cities.append(city)
            return _cities

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan")
