#!/usr/bin/python3
import requests
import sys

try:
    if len(sys.argv) < 2:
        s = ""
    else:
        s = sys.argv[1]
    data = {'q': s}
    url = 'http://0.0.0.0:5000/search_user'
    responses = requests.post(url, data)
    responses = responses.json()
    if responses:
        print("[{}] {}".format(responses.get('id'), responses.get('name')))
    else:
        print("No result")
except Exception:
    print("Not a valid JSON")
