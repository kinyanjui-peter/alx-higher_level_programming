#!/bin/bash
# script that get URL, sends a request to that URL, and displays the size of the body of the response
#respoce_size=$(curl -I "$1" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r\n')
response_size=$(curl -s "$url" | wc -c)
