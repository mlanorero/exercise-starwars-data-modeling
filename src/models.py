import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
# uno a muchos, una persona puede tener hartas emails
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Email_Address(Base):
    __tablename__ = 'email_adres'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email_user = Column(String(250))
    simbol = Column(String(250))
    email_domain = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

# uno a uno, una persona puede tener una cuenta en el blog

class Username(Base):
    __tablename__= 'username'
    id = Column(Integer, primary_key=True)
    email_user = Column(String(250))
    username = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

# uno a mucho, un usuario o persona puede guardar muchos personajes favoritos

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    email_user = Column(String(250))
    username = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Username)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')