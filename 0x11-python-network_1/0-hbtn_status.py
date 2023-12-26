#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
You must use a with statement
"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

def read_url(url):
    with urllib.request.urlopen(url) as req:
        content = req.read()
        print("Body response:")
        print("\t- type:\n", type(content))
        print("\t- content:\n", content)
        print("\t- utf8 content:\n", content.decode('utf-8'))
if __name__ == "__main__":
    read_url(url)    
