###file2db.py repository

https://travis-ci.org/karmab/file2db.svg?branch=master
[![Build Status](https://travis-ci.org/karmab/file2db.svg?branch=master)](https://travis-ci.org/karmab/file2db)
[![Code Climate](https://codeclimate.com/github/karmab/file2db/badges/gpa.svg)](https://codeclimate.com/github/karmab/file2db)


This script allows to sync content between a table within a database and flat files

## Install

```bash
pip install -r https://raw.githubusercontent.com/karmab/file2db/master/requirements.txt
```

##Contents

-    `README.md` this file
-    `file2db.py`  downloads content from a DB table in local files
-    `extra/Dockerfile`  if it doesnt run as a docker, you re nobody

## How to use

copy settings.py to current directory and edit accordingly
launch with 
./file2db.py 


# Docker all the things

```bash
cd extra
docker build --rm -t file2db ./
# Use settings.py.docker from samples dir and rename it settings.py somewhere. For instance,
docker run -p 9000:9000 -t -d -i --name=file2db -v $HOME/file2db/data:/opt/file2db/data -v $HOME/file2db/settings.py:/opt/file2db/settings.py file2db
```

# Client operation
#retrieve data from DB
curl http://YOUR_IP:YOUR_PORT
#update data to DB
curl -X POST http://YOUR_IP:YOUR_PORT

# Problems?

Send me a mail at [karimboumedhel@gmail.com](mailto:karimboumedhel@gmail.com) !

Mac Fly!!!

karmab
