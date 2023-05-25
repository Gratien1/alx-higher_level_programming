#!/usr/bin/python3
"""
Python package urllib usiing for HTTP requests
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    param = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(param).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode())
