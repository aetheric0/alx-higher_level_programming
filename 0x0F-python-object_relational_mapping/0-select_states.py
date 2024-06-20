#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    c = db.cursor()
    c.execute('SELECT * FROM states ORDER BY id ASC')
    for row in c.fetchall():
        print(row)
