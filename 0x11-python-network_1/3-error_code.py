#!/usr/bin/python3
""" retrieves the body of the url and handles exceptions
"""

if __name__ == '__main__':
    from urllib import request, error
    from sys import argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read())
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
