#!/usr/bin/python3
"""
Prints the state row that matches the argument given
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], password=argv[2], db=argv[3])
    c = db.cursor()
    c.execute('SELECT * from states WHERE name = %s', (argv[4],))
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
