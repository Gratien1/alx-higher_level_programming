#!/usr/bin/python3
"""
Python package urllib usiing for HTTP requests
"""
from urllib.request import urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            html = response.read()
            print(html.decode())
    except HTTPError as e:
        print(f"Error code: {e.code}")
