#!/usr/bin/python3
"""
Python package urllib usiing for HTTP requests
"""


if __name__ == "__main__":
    import urllib.request as url_req
    import sys
    with url_req.urlopen(sys.argv[1]) as response:
        var = response.headers.get("X-Request-Id")
        print(var)
