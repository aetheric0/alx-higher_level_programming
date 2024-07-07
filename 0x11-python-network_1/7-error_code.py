#!/usr/bin/python3
""" Gets and displays body of URL and prints status codes
for codes greater than or equal to 400 using requests module
"""

if __name__ == '__main__':
    from sys import argv
    import requests
    url = argv[1]
    req = requests.get(url)
    if (req.status_code) >= 400:
        print(req.status_code)
    else:
        print(req.text)
