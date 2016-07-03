FROM debian
MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>

RUN apt-get update && apt-get install -y git gettext-base python-setuptools python-dev gcc libpq-dev && easy_install pip && apt-get clean
RUN pip install -r https://raw.githubusercontent.com/karmab/file2db/master/requirements.txt
RUN git clone https://github.com/karmab/file2db.git /opt/file2db
RUN cd  /opt/file2db && git pull
RUN chmod u+x /opt/file2db/file2db.py
EXPOSE 9000
ENTRYPOINT ["/opt/file2db/file2db.py"]
