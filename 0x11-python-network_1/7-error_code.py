#!/usr/bin/python3
"""
Module
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with requests.get(url) as response:
            body = response.text
            print(body)
    except requests.HTTPError as e:
        if e.response is not None and e.response.status_code >= 400:
            print("Error code: {}".format(e.response.status_code))
