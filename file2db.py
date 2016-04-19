#!/usr/bin/python

from flask import Flask
import os
from sqlalchemy import create_engine, Column, Integer, MetaData, Table, update
from sqlalchemy.orm.session import make_transient
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import mapper, sessionmaker


app = Flask(__name__)
app.config.from_object('settings')


class TABLE(object):
    pass


@app.route("/get")
def get():
    """
    retrieves files from database definition
    """
    table = app.config['DATA']['table']
    path = app.config['DATA']['path'] if 'path' in app.config['DATA'].keys() else '.'
    key = app.config['DATA']['key'] if 'key' in app.config['DATA'].keys() else 'id'
    name = app.config['DATA']['name'] if 'name' in app.config['DATA'].keys() else 'name'
    content = app.config['DATA']['content'] if 'content' in app.config['DATA'].keys() else 'content'
    engine = create_engine(URL(**app.config['DATABASE']))
    maker = sessionmaker(bind=engine)
    session = maker()
    metadata = MetaData(engine)
    table = Table(table, metadata, Column(key, Integer, primary_key=True), autoload=True)
    try:
        mapper(TABLE, table)
    except:
        pass
    results = session.query(TABLE).all()
    for entry in results:
        filename = getattr(entry, name)
        entrypath = "%s/%s" % (path, filename)
        with open(entrypath, 'w') as f:
            f.write(getattr(entry, content))
    return "GET OK"


@app.route("/post")
def post():
    """
    sends files to database
    :return:
    """
    table = app.config['DATA']['table']
    path = app.config['DATA']['path'] if 'path' in app.config['DATA'].keys() else '.'
    key = app.config['DATA']['key'] if 'key' in app.config['DATA'].keys() else 'id'
    name = app.config['DATA']['name'] if 'name' in app.config['DATA'].keys() else 'name'
    content = app.config['DATA']['content'] if 'content' in app.config['DATA'].keys() else 'content'
    engine = create_engine(URL(**app.config['DATABASE']))
    maker = sessionmaker(bind=engine)
    session = maker()
    metadata = MetaData(engine)
    fileslist = os.listdir(path)
    table = Table(table, metadata, Column(key, Integer, primary_key=True), autoload=True)
    try:
        mapper(TABLE, table)
    except:
        pass
    allentries = session.query(TABLE).all()
    first = allentries[0]
    maxid = max([getattr(a, key) for a in allentries])
    session.expunge(first)
    make_transient(first)
    counter = maxid
    for entry in fileslist:
        entrypath = "%s/%s" % (path, entry)
        with open(entrypath, 'r') as f:
            entrycontent = f.read()
        x = [a for a in allentries if getattr(a, name) == entry]
        if len(x) > 0:
            u = update(table).where(table.c.name == entry).values({content: entrycontent})
            session.execute(u)
        else:
            counter += counter
            setattr(first, key, counter)
            setattr(first, name, entry)
            setattr(first, content, entrycontent)
            session.add(first)
            session.flush()
        session.commit()
    return "POST OK"

if __name__ == '__main__':
    app.run(host=0.0.0.0,port=9000, debug=True)
