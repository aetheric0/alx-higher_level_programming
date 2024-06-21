#!/usr/bin/python3
"""
Prints the cities associated with a state given as an argument
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    dbase_name = argv[3]
    state = argv[4]

    db = MySQLdb.connect('localhost', user, password, dbase_name)
    c = db.cursor()
    c.execute('SELECT cities.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s', (state,))
    print(', '.join(row[0] for row in c.fetchall()))

    c.close()
    db.close()
