
from sqlalchemy import create_engine, Column, Integer, MetaData, Table
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import mapper, sessionmaker
import settings


class VMS(object):
    pass

engine = create_engine(URL(**settings.DATABASE))
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData(engine)
vms = Table('vms', metadata, Column("vm_guid", Integer, primary_key=True), autoload=True)
mapper(VMS, vms)
results = session.query(VMS).all()
vms = [vm.vm_name for vm in results]
print vms
