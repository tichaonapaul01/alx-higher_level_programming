#!/usr/bin/python3
import requests
import sys

try:
    respon = requests.get(sys.argv[1])
    head = respon.headers['X-Request-Id']
    print(head)
except BaseException:
    pass
