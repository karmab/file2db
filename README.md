###file2db.py repository

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

TBD


# Docker all the things

```bash
cd extra
docker build --rm -t file2db ./
#docker run -p 9000:9000 -t -d -i --name=file2db file2db

export FILE2DBSETTINGS=$HOME/file2db/settings.cfg
sudo docker run -p 9000:9000 -t -d -i --name=file2db -v $HOME/file2db/data:/opt/file2db/data -v $HOME/file2db/settings.cfg:/opt/file2db/settings.cfg file2db
```

# Problems?

Send me a mail at [karimboumedhel@gmail.com](mailto:karimboumedhel@gmail.com) !

Mac Fly!!!

karmab
