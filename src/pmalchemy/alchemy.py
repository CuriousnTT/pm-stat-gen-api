import sqlalchemy
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

DATABASE_PATH = "pmdb/pmdb.sqlite3"

engine = sqlalchemy.create_engine(f"sqlite+pysqlite:///{DATABASE_PATH}", echo=True)
metadata_obj = Base.metadata

Session = sessionmaker(bind=engine)
session = Session()

def show_all_tables():
    metadata_obj.reflect(bind=engine)

def clean_database():
    metadata_obj.drop_all(bind=engine)

def make_database():
    metadata_obj.create_all(engine)