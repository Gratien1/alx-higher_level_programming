#!/usr/bin/python3
"""
Python package requests usiing for HTTP requests
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t-", f"type: {type(r.text)}")
    print("\t-", f"content: {r.text}")
