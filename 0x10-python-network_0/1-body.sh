#!/bin/bash
# takes in a URL, sends a GET request to the URL, and stores the body and status code in an array
readarray -t response < <(curl -s -w "\n%{http_code}" "$1") && [ "${response[-1]}" -eq 200 ] && curl -s "$1"
