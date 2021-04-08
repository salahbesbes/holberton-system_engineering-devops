#!/bin/bash
# using curl command to pink an URL and print the content-length of the response
echo $"$(curl -sI "$1" | grep 'Content-Length' | cut  -d ':' -f '2' | cut -d ' ' -f '2')"
