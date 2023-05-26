#!/bin/bash

docker ps -a | grep "mysql" | awk '{print $1}' | xargs docker rm -f