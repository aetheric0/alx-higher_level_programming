#!/usr/bin/bash
# Gets the size of body of response
socket=$1
curl -sI "$socket" | grep -i 'Content-Length' | awk '{print $2}'
