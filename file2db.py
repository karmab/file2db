#!/usr/bin/python

import getpass
from mock import patch
from flask import Flask
import os
from sqlalchemy import create_engine, Column, Integer, MetaData, Table, update
from sqlalchemy.orm.session import make_transient
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import mapper, sessionmaker

app = Flask(__name__)
try:
    app.config.from_object('settings')
    config = app.config
except ImportError:
    data = {}
    data['table'] = os.environ.get('TABLE')
    data['datapath'] = os.environ.get('DATAPATH')
    data['id'] = os.environ.get('ID')
    data['name'] = os.environ.get('NAME')
    data['content'] = os.environ.get('CONTENT')
    config = {'DATA': data}
    database = {}
    database['drivername'] = os.environ.get('DBDRIVER')
    database['host'] = os.environ.get('DBHOST')
    database['port'] = os.environ.get('DBPORT')
    database['username'] = os.environ.get('DBUSERNAME')
    database['password'] = os.environ.get('DBPASSWORD')
    database['database'] = os.environ.get('DBNAME')
    config['DATABASE'] = database
    config['DEBUG'] = os.environ.get('DEBUG')
    config['PORT'] = os.environ.get('PORT', 9000)

debug = config['DEBUG'] if 'DEBUG' in config.keys() else True
port = int(config['PORT']) if 'PORT'in config.keys() else 9000


class TABLE(object):
    pass


@app.route("/", methods=['GET'])
def get():
    """
    retrieves files from database definition
    """
    table = config['DATA']['table']
    datapath = config['DATA']['datapath'] if 'datapath' in config['DATA'].keys() else '.'
    key = config['DATA']['key'] if 'key' in config['DATA'].keys() else 'id'
    name = config['DATA']['name'] if 'name' in config['DATA'].keys() else 'name'
    content = config['DATA']['content'] if 'content' in config['DATA'].keys() else 'content'
    engine = create_engine(URL(**config['DATABASE']))
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
        entrypath = "%s/%s" % (datapath, filename)
        with open(entrypath, 'w') as f:
            f.write(getattr(entry, content))
    return "GET OK"


@app.route("/", methods=['POST'])
def post():
    """
    sends files to database
    :return:
    """
    table = config['DATA']['table']
    datapath = config['DATA']['datapath'] if 'datapath' in config['DATA'].keys() else '.'
    key = config['DATA']['key'] if 'key' in config['DATA'].keys() else 'id'
    name = config['DATA']['name'] if 'name' in config['DATA'].keys() else 'name'
    content = config['DATA']['content'] if 'content' in config['DATA'].keys() else 'content'
    engine = create_engine(URL(**config['DATABASE']))
    maker = sessionmaker(bind=engine)
    session = maker()
    metadata = MetaData(engine)
    fileslist = os.listdir(datapath)
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
        entrypath = "%s/%s" % (datapath, entry)
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
    with patch.object(getpass, "getuser", return_value='default'):    
        app.run(host='0.0.0.0', port=port, debug=debug)
