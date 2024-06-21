#!/usr/bin/python3
""" Prints state, city.id city from the states and cities tables \
ordered by City id
"""
from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    db_object = session.query(City).join(City.state).order_by(City.id).all()
    for row in db_object:
        print('{}: ({}) {}'.format(row.state.name, row.id, row.name))
