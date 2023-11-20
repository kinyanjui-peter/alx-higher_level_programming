#!/usr/bin/python3
"""
Write a python file that contains the class definition of a State and an instance Base = declarative_base():

State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
class attribute name that represents a column of a string with maximum 128 characters and can’t be null
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost at port 3306
WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = 'mysql://localhost:3306/states'

#map classes to tables
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key = True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

#Create an engine to connect to the MYSQL server
engine = create_engine(database_url, echo=True)#set  echo=True for debugging

#create tables inthe database
Base.metadata.create_all(engine)

#create a session to nteract with database
Session = sessionmaker(bind=engine)
session = Session()

#url,map,model,connect,table,sessionbind
