#!/bin/bash
# Gets the body of the response
curl -sIX OPTIONS "$1" | grep -i "Allow" | awk "{print $2}"
