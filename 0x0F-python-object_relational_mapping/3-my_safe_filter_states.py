#!/usr/bin/python3
"""
Prints the state row that matches the state passed as an argument
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    c = db.cursor()
    c.execute('SELECT * from states WHERE name = %s', (argv[4],))
    for row in c.fetchall():
        print(row)

    c.close()
    db.close()
