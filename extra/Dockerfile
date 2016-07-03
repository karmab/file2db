FROM alpine:latest
MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>

RUN apk add --update musl build-base python3 python3-dev git py-pip  postgresql-dev python-dev
RUN rm -rf /var/cache/apk
RUN cd /usr/bin && ln -sf easy_install-3.4 easy_install && ln -sf idle3.4 idle && ln -sf pydoc3.4 pydoc && ln -sf python3.4 python && ln -sf python-config3.4 python-config && ln -sf pip3.4 pip
RUN 
RUN pip install -r https://raw.githubusercontent.com/karmab/file2db/master/requirements.txt
RUN git clone https://github.com/karmab/file2db.git /opt/file2db
RUN cd  /opt/file2db && git pull
RUN chmod u+x /opt/file2db/file2db.py

EXPOSE 9000

ENTRYPOINT ["/opt/file2db/file2db.py"]
