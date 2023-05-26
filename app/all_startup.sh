#!/bin/bash

docker-compose down --rmi all
docker-compose build --pull api
docker-compose build --pull mysql
docker volume rm $(docker volume ls -qf dangling=true)
docker-compose up -d