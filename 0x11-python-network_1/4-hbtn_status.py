#!/usr/bin/python3
""" Uses requests modult to fetch url
"""

if __name__ == '__main__':
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}\n\t- content: {}'.format(type(req.text), req.text))
