#!/usr/bin/python3
""" Takes in a letter as parameter and sends a POST request to url
"""

if __name__ == '__main__':
    from sys import argv
    import requests
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        req = requests.post(url, data ={'q': argv[1]})
    else:
        req = requests.post(url, data ={'q': ""})
    try:
        a = req.json()
        if a:
            print('[<{}>] <{}>'.format(a['id'], a['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
