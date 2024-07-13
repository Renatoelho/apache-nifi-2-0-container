#!/bin/bash

docker run --name nifi --rm \
  -p 8443:8443 \
  -e SINGLE_USER_CREDENTIALS_USERNAME=nifi \
  -e SINGLE_USER_CREDENTIALS_PASSWORD=HGd15bvfv8744ghbdhgdv7895agqERAo \
  apache/nifi:2.0.0-M4