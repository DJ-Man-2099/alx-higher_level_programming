#!/bin/bash
<<<<<<< HEAD
# takes in a URL, sends a GET request to the URL, and stores the body and status code in an array
readarray -t response < <(curl -s -w "\n%{http_code}" "$1") && [ "${response[-1]}" -eq 200 ] && curl -s "$1"
=======
# takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s "$1"
>>>>>>> 7f5b79be688c6b8b9189682fddf213a830604fca
