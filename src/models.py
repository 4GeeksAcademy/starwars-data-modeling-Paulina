import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    favourites = relationship("Favourites", backref='User')

class Favourites(Base):
    __tablename__ = 'Favourites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    height = Column(Integer, nullable=False)
    hair_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False) 
    birth_day = Column(String(50), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    character_id = Column(String(255), ForeignKey("character.id"))
    planets_fav = relationship("Favourites", backref = "planets")

    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
