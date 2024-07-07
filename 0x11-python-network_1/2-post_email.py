#!/usr/bin/python3
""" Uses the POST request method on the passed URL
"""

if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv
    url = argv[1]
    email = {'email': argv[2]}
    email = parse.urlencode(email)
    email = email.encode('ascii')
    req = request.Request(url, email)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
