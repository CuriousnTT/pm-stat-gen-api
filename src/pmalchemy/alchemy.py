import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Integer, String, Column, MetaData

DATABASE_PATH = "pmdb/pmdb.sqlite3"
Base = declarative_base()

engine = sqlalchemy.create_engine(f"sqlite+pysqlite:///{DATABASE_PATH}", echo=True)
metadata_obj = Base.metadata

def show_all_tables():
    metadata_obj.reflect(bind=engine)

def reflect_database():
    metadata_obj.drop_all(bind=engine)

def make_database():
    metadata_obj.create_all(engine)