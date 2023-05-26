#!/bin/bash

docker-compose stop api
# docker images | grep "<none>" | awk '{print $3}' | xargs docker rmi -f
docker-compose build --pull api
docker-compose create api
docker-compose start api
docker image prune -f