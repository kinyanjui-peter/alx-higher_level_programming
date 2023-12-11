#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sV "$1" | grep -i http
