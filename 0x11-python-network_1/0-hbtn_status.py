#!/usr/bin/python3
"""
Python package urllib usiing for HTTP requests
"""


if __name__ == "__main__":
    import urllib.request as url_req
    with url_req.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t-", f"type: {type(html)}")
        print("\t-", f"content: {html}")
        print("\t-", f"utf8 content: {html.decode('utf8')}")
