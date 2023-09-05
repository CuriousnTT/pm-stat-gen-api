import sqlalchemy
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

DATABASE_PATH = "pmdb/pmdb.sqlite3"

engine = sqlalchemy.create_engine(f"sqlite+pysqlite:///{DATABASE_PATH}")
metadata_obj = Base.metadata

Session = sessionmaker(bind=engine)
session = Session()

def commit_and_close():
    try:
        session.commit()
    except Exception as e:
        print(f"Error committing changes to database: {e}")
        session.rollback()
    finally:
        session.close()

def show_all_tables():
    metadata_obj.reflect(bind=engine)

def clean_database():
    metadata_obj.drop_all(bind=engine)

def make_database():
    metadata_obj.create_all(engine)

def get_all_from_table(cls):
    try:
        return session.query(cls).all()
    except Exception as error:
        print(f"Error contacting {cls.__tablename__} table: {error}")
        session.rollback()