import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Table, Integer, String, Column, MetaData

class Base(DeclarativeBase):
    pass

engine = sqlalchemy.create_engine("sqlite+pysqlite:///:memory:", echo=True)
metadata_obj = Base.metadata
generation = Table(
        "generation",
        metadata_obj,
        Column("genNr", Integer)
    )
pm_dex = Table(
        "pmDex",
        metadata_obj,
        Column("pmDexNr", Integer, primary_key=True),
        Column("pmName", String(45), unique=True),
        Column("gender", Integer),
    )

Base.metadata.create_all(engine)