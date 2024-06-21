#!/usr/bin/python3
""" Updates the state with id of 2 to New Mexico
"""
from sys import argv
from model_state import Base, State
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
    update_state = session.query(State).filter(State.id == 2).first()
    update_state.name = 'New Mexico'
    session.commit()
