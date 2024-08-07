#!/usr/bin/python3
""" Displays the header X-Request-Id value in the response header
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    req = requests.get(argv[1])
    print(req.headers['X-Request-Id'])
