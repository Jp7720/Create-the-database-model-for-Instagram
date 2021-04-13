import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100))
    password = Column(String(100))
    age = Column(Integer)
    followers_id = Column(Integer, ForeignKey('followers.id'))
    
    

class Likes(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer)
    posts_id = Column(Integer, ForeignKey('posts.id'))
    users_id = Column(Integer, ForeignKey('users.id'))

    

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    followers_id = Column(Integer)
    user_id = Column(Integer)
    accepted = Column(String(10))
    users_id = Column(Integer, ForeignKey('users.id'))


class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer)
    created_at = Column(String(250))
    photo = Column(String(250), nullable=False)
   
    comments_id = Column(String, ForeignKey('comments.id'))
    users_id = Column(Integer, ForeignKey('users.id'))


class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer)
    post_id = Column(Integer)
    content = Column(String(250), nullable=False)
    created_at = Column(String(100))

    users_id = Column(Integer, ForeignKey('users.id'))





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')