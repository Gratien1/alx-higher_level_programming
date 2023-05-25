#!/usr/bin/python3
"""
Python package requests usiing for HTTP requests
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {password}"}
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        user_data = r.json()
        print(user_data['id'])
    else:
        print('None')
