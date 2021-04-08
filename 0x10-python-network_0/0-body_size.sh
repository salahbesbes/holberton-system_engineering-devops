#!/bin/bash
# using curl command to pink an URL and print the content-length of the
# response

URL=$1
response=$(curl -sI "$URL")
res=$( echo "$response" | grep 'Content-Length' | cut  -d ':' -f '2' | cut -d ' ' -f '2')
echo "$res"

