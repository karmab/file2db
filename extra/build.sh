#!/bin/bash
#sample script to clean image

for container in `docker ps -q --filter="image=file2db:latest"` ; do docker stop $container ; docker rm $container ; done
docker rmi file2db
docker build --rm -t file2db ./
