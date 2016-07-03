#!/bin/bash
#sample script to clean image

#for container in `docker ps -q --filter="image=karmab/file2db:latest"` ; do docker stop $container ; docker rm $container ; done
docker stop file2db
docker rm file2db
docker rmi karmab/file2db
docker build --rm -t karmab/file2db ./
