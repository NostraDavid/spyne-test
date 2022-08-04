#!/usr/bin/env bash

# Somewhat works
curl -X POST http://localhost:8000/say_hello?name=Dave\&times=3

# doesn't work (yet?)
# curl -X POST  --header "Content-Type: text/xml;charset=UTF-8" --header "SOAPAction: ACTION_YOU_WANT_TO_CALL" http://localhost:8000/ 
