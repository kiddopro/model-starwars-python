import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    class Character(Base):
        __tablename__ = 'character'
        id = Column(Integer, primary_key=True)
        uid = Column(String(4))
        name = Column(String(250))
        height = Column(String(250))
        mass = Column(String(250))
        hair_color = Column(String(250))
        eye_color = Column(String(250))
        birth_year = Column(String(250))
        gender = Column(String(250))
        description = Column(String(250))


    class Planet(Base):
        __tablename__ = 'planet'
        id = Column(Integer, primary_key=True)
        uid = Column(String(4))
        name = Column(String(250))
        diameter = Column(String(250))
        population = Column(String(250))
        terrain = Column(String(250))
        climate = Column(String(250))
        surface_water = Column(String(1))
        rotation_period = Column(String(250))
        orbital_period = Column(String(250))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    password = Column(String(250))
    email = Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')