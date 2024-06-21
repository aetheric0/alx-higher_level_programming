#!/usr/bin/python3
"""Adds a new State as well as the city/cities associated with it \
using the relationship class
"""
from sys import argv
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased, relationship

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name='California', cities='San Francisco')
    session.add(state)
    session.commit()
