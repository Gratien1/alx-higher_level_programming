#!/usr/bin/python3
"""
Python package requests usiing for HTTP requests
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    value = sys.argv[1] if len(sys.argv) >= 2 else ""
    param = {'q': value}
    r = requests.post(url, data=param)
    if 'application/json' in r.headers.get('content-type'):
        json_r = r.json()
        if not json_r:
            print('No result')
        else:
            print(f"[{json_r['id']}] {json_r['name']}")
    else:
        print('Not a valid JSON')
