#!/usr/bin/python3
""" Script that fetches url
"""
if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv
    url = argv[1]
    with request.urlopen(url) as response:
        header = response.info()
        print(header['X-Request-Id'])
