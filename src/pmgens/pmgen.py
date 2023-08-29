from enum import Enum
from pmalchemy.alchemy import Base, session
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

class PmGen(Enum):
    GEN1 = "gen1"
    GEN2 = "gen2"
    GEN3 = "gen3"
    GEN4 = "gen4"
    GEN5 = "gen5"
    GEN6 = "gen6"
    GEN7 = "gen7"
    GEN8 = "gen8"
    GEN9 = "gen9"

class SupportedGen(str, Enum):
    GEN1 = "gen1"

class Generation(Base):
    __tablename__ = "generation"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    short_name: Mapped[str] = mapped_column(String(5), unique=True)

    def __init__(self, name, short_name):
        self.name = name
        self.short_name = short_name
    
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.short_name
    
def getGenerationsTable():
    id = 0
    for x in list(PmGen):
        id += 1
        name = f"generation{id}"
        generation = session.query(Generation).filter_by(id=id).first()
        if generation is None:
            session.add(Generation(name=name, short_name=x.value))
    session.commit()

def isSupported(gen: PmGen):
        if gen in list(SupportedGen):
            return True
        else:
            return False