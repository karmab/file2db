
import os
from sqlalchemy import create_engine, Column, Integer, MetaData, Table, update
from sqlalchemy.orm.session import make_transient
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import mapper, sessionmaker
import settings
import sys


class TABLE(object):
    pass


class File2db:
    def __init__(self):
        try:
            self.table = settings.DATA['table']
        except KeyError:
            print 'missing Table from configuration'
            sys.exit(1)
        self.path = settings.DATA['path'] if 'path' in settings.DATA.keys() else '.'
        self.key = settings.DATA['key'] if 'key' in settings.DATA.keys() else 'id'
        self.name = settings.DATA['name'] if 'name' in settings.DATA.keys() else 'name'
        self.content = settings.DATA['content'] if 'content' in settings.DATA.keys() else 'content'
        engine = create_engine(URL(**settings.DATABASE))
        maker = sessionmaker(bind=engine)
        self.session = maker()
        self.metadata = MetaData(engine)

    def get(self):
        path = self.path
        session = self.session
        metadata = self.metadata
        table = self.table
        key = self.key
        name = self.name
        content = self.content
        table = Table(table, metadata, Column(key, Integer, primary_key=True), autoload=True)
        mapper(TABLE, table)
        results = session.query(TABLE).all()
        for entry in results:
            filename = getattr(entry, name)
            entrypath = "%s/%s" % (path, filename)
            with open(entrypath, 'w') as f:
                f.write(getattr(entry, content))

    def post(self):
        path = self.path
        fileslist = os.listdir(path)
        session = self.session
        metadata = self.metadata
        table = self.table
        key = self.key
        name = self.name
        content = self.content
        table = Table(table, metadata, Column(key, Integer, primary_key=True), autoload=True)
        mapper(TABLE, table)
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

if __name__ == '__main__':
    conn = File2db()
    conn.post()
