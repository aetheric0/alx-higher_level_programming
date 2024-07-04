#!/bin/bash
# Posts to the server thee variables email and subject
curl -so /dev/null -w "%{http_code}" "$1"
