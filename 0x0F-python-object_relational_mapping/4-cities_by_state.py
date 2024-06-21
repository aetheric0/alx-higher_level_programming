#!/usr/bin/python3
"""
Prints both the state and city associated with the state
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    dbase_name = argv[3]

    db = MySQLdb.connect('localhost', user, password, dbase_name)
    c = db.cursor()
    c.execute('SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON state_id = states.id')
    for row in c.fetchall():
        print(row)

    c.close()
    db.close()
