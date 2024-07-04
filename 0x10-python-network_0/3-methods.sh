#!/bin/bash
# Gets the body of the response
curl -sIX "$1" | grep -i "Allow" | awk "{print $2}"
