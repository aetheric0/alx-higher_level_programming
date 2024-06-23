#!/usr/bin/python3
""" Prints States and the cities that falls under the state
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_and_city = session.query(
        State
    ).filter(
        State.id == City.state_id
    ).order_by(State.id)
    session.commit()
    for row in state_and_city:
        print('{}: {}'.format(row.cities[0].state.id, row.cities[0].state.name))
        for city in row.cities:
            print('\t{}: {}'.format(city.id, city.name))
