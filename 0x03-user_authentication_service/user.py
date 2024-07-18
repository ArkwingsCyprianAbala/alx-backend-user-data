#!/usr/bin/env python3
"""
Module for creating user database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    """
    Creates tables for users
    """

    __tablename__:str = "users"

    id = Column(Integer, primary_key = True, autoincrement = True)
    email = Column(String(250), nullable = False)
    hashed_password = Column(String(250), nullable = False)
    session_id = Column(String(250), nullable = True)
    reset_token = Column(String(250), nullable = True)
