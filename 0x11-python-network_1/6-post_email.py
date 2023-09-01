#!/usr/bin/python3
import requests
import sys

try:
    my_data = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], my_data)
    print(res.text)
except BaseException:
    pass
