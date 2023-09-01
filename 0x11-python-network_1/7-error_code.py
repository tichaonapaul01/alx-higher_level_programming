#!/usr/bin/python3
import requests
import sys

try:
    respon = requests.get(sys.argv[1])
    if respon.status_code == requests.codes.ok:
        print(respon.text)
    else:
        if respon.status_code >= 400:
            print("Error code:", respon.status_code)
except BaseException:
    pass
