#!/usr/bin/python3
"""
    Python script that takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and displays
    the body of the response (decoded in utf-8)
    The email must be sent in the email variable
    You must use the packages urllib and sys
    You are not allowed to import packages other than urllib and sys
    You don’t need to check arguments passed to the script (number or type)
    You must use the with statement
    """
import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    # Encode the data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a POST request object
    request = urllib.request.Request(url, data=data, method='POST')

    # Send the request and get the response
    with urllib.request.urlopen(request) as response:
        # Read and print the response body
        content = response.read().decode('utf-8')
        print(content)

if __name__ == "__main__":
    # Get the URL and email from the command line arguments
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

url_to_post = sys.argv[1]
email_to_send = sys.argv[2]

send_post_request(url_to_post, email_to_send)     
