#!/usr/bin/bash
# Gets the size of body of response
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
