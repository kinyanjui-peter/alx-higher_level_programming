#!/usr/bin/python3
"""
Write a script that lists all State objects from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported"""

import sys
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if len(sys.argv) != 4:
    sys.exit(1)

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
mysql_database_name = sys.argv[3]


#url,map,model,connect,table,sessionbind
database_url = 'mysql+mysqldb://{}:{}@localhost:3306/hbtn_0e_6_usa'.format(mysql_username, mysql_password, mysql_database_name)

#map
Base = declarative_base()

#model
class States(Base):
    __tablename__= 'States'

    username = Column(String)
    password = Column(Integer)
    name = Column(String)
    id = column(Integer, primary_key=True)

if __name__ == "__main__":
    engine = create_engine(database_url, echo=True)
    
    #create table
    base.metadata.create_all(engine)

    #session
    Session = sessionmaker(bind=engine)
    session = Session()

    sorted_by_id = session.query(States).order_by(State.id).all()

    for state in sorted_by_id:
        print(f"ID: {State.id}, Name: {state.name}, Username:(State.username), passwoerd:{State.password}")

    session.close()










