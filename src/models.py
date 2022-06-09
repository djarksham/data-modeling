import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    mail = Column(String(30))
    favoritos = relationship("Favorito")

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    typed = Column(String(20))
    dimension = Column(String(20))
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character", back_populates="characters")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    status = Column(String(20))
    species = Column(String(20))
    gender = Column(String(20))
    characters = relationship("Location")
    characters_e = relationship("Episode")
    favorito_id = Column(Integer, ForeignKey("favorito.id"))
    location_id = Column(Integer, ForeignKey("location.id"))
    episode_id = Column(Integer, ForeignKey("episode.id"))

class Episode(Base):
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    air_date = Column(String(20))
    species = Column(String(20))
    episode = Column(String(20))
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character", back_populates="characters_e")




    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e