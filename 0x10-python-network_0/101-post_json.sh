#!/bin/bash
# Gets the body of the response
curl -X POST -sH "Content-Type: application/json" --data-binary "@2" "$1"
