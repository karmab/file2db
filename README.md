# file2db.py repository

[![Build Status](https://travis-ci.org/karmab/file2db.svg?branch=master)](https://travis-ci.org/karmab/file2db)
[![Code Climate](https://codeclimate.com/github/karmab/file2db/badges/gpa.svg)](https://codeclimate.com/github/karmab/file2db)


This script allows to sync content between a table within a database and flat files

## Install

```bash
pip install -r https://raw.githubusercontent.com/karmab/file2db/master/requirements.txt
```

## Contents

-    `README.md` this file
-    `file2db.py`  downloads content from a DB table in local files
-    `extra/Dockerfile`  if it doesnt run as a docker, you re nobody

## How to use

copy settings.py to current directory and edit accordingly
you can alternatively use the following environment variables
- DATAPATH path where to store the synced table. Defaults to '.'
- ID primary key of the table. Defaults to 'id'
- NAME field of the table to name files after. Defaults to name
- CONTENT
- DBDRIVER Type of db. Allowed values are postgresql,sqlite3 and mysql
- DBHOST
- DBPORT
- DBUSERNAME
- DBPASSWORD
- DBNAME
- DBTABLE    
- DEBUG defaults to True
- PORT  defaults to 9000

launch with 
./file2db.py 


## Docker all the things

```bash
cd extra
docker build --rm -t file2db ./
# Use settings.py.docker from samples dir and rename it settings.py somewhere. For instance,
docker run -p 9000:9000 -t -d -i --name=file2db -v $HOME/file2db/data:/opt/file2db/data -v $HOME/file2db/settings.py:/opt/file2db/settings.py karmab/file2db
# For env variables launch
docker run -p 9000:9000 -t -d -i --name=file2db -v $HOME/file2db/data:/opt/file2db/data -e KEY=id -e NAME=name -e CONTENT=content -e DBDRIVER=postgresql -e DBHOST=192.168.3.1 -e DBPORT=5432 -e DBUSERNAME=testk -e DBPASSWORD=testk -e DBNAME=testk -e DBTABLE=mytemplates -e PORT=9000 -e DEBUG=True -e DATAPATH=/opt/file2db/data karmab/file2db

```

##  Client operation
```bash
curl http://YOUR_IP:YOUR_PORT
curl -X POST http://YOUR_IP:YOUR_PORT
```

## Problems?

Send me a mail at [karimboumedhel@gmail.com](mailto:karimboumedhel@gmail.com) !

Mac Fly!!!

karmab
