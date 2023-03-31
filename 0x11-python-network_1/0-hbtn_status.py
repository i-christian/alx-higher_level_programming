#!/usr/bin/python3
from urllib.request import urlopen
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""


with urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()

if __name__ == "__main__":
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
