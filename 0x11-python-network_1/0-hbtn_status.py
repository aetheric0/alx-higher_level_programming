#!/usr/bin/python3
""" Script that fetches url
"""
if __name__ == '__main__':
    from urllib import request, parse
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
            type(body), body, body.decode('utf-8')))
