#!/usr/bin/python3
""" Posts a POST request to the URL for an email
"""

if __name__ == '__main__':
    from sys import argv
    import requests
    url = argv[1]
    email = argv[2]
    req = requests.post(url, data={'email': email})
