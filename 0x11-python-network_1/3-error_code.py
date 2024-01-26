#!/usr/bin/python3
"""
Module
"""
import sys
import urllib.request as request
import urllib.parse as parse
import urllib.error as error

if __name__ == "__main__":
    url = sys.argv[1]
    body = {
        'email': sys.argv[2]
    }
    parsed_data = parse.urlencode(body).encode('ascii')
    req = request.Request(url, parsed_data)
    try:
        with request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
