#!/usr/bin/python3
""" Prints the city and the State of which the city is a part of
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(
        City
    ).filter(
        City.state_id == State.id
    ).order_by(
        City.id
    )
    for city in data:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
