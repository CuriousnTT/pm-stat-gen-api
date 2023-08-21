import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Table, Integer, String, Column, MetaData

DATABASE_PATH = "pmdb/pmdb.sqlite3"

class Base(DeclarativeBase):
    pass

engine = sqlalchemy.create_engine(f"sqlite+pysqlite:///{DATABASE_PATH}", echo=True)
metadata_obj = Base.metadata
generation = Table(
        "generation",
        metadata_obj,
        Column("genNr", Integer)
    )
#pm_dex = Table(
#        "pmDex",
#        metadata_obj,
#       Column("pmDexNr", Integer, primary_key=True),
#        Column("pmName", String(45), unique=True),
#        Column("gender", Integer),
#    )
def show_all_tables():
    metadata_obj.reflect(bind=engine)

def reflect_database():
    metadata_obj.drop_all(bind=engine)

def make_database():
    metadata_obj.create_all(engine)