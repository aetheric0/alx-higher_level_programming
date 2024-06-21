#!/usr/bin/python3
"""Prints only states that begin with N in the states table
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    engine = MySQLdb.connect(host='localhost', port='3306',
                             user=argv[1], password=argv[2], db=argv[3])
    c = engine.cursor()
    c.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC')
    for row in c.fetchall():
        print('{}'.format(row))
    c.close()
    engine.close()
