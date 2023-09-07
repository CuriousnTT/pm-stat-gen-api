from enum import Enum
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from pmalchemy.alchemy import Base, session, commit_and_close, get_all_from_table
from migrations.initialize import generations

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
    name: Mapped[str] = mapped_column(String(5), unique=True)
    start_year: Mapped[int] = mapped_column(Integer)
    end_year: Mapped[int] = mapped_column(Integer, nullable=True)
    type_chart_id: Mapped[int] = mapped_column(Integer, ForeignKey('type_charts.id'))

    def __init__(self, id: int, name: str, start_year: int, end_year: int, pm_type_chart_id: int):
        self.id = id
        self.name = name
        self.start_year = start_year
        self.end_year = end_year
        self.type_chart_id = pm_type_chart_id
    
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.name
    
def isSupported(gen: PmGen):
        if gen in list(SupportedGen):
            return True
        else:
            return False
    
def getGenerationsTable():
    id = 0
    for gen in list(PmGen):
        gen_dict = generations[gen.value]
        id += 1
        try:
            generation = session.query(Generation).filter_by(id=id).first()
            if generation is None:
                generation = Generation(
                    id=id,
                    name=gen.value,
                    start_year=gen_dict["start_year"],
                    end_year=gen_dict["end_year"],
                    pm_type_chart_id=gen_dict["type_chart"]
                    )
                session.add(generation)
        except Exception as error:
            print(f"Error adding generation to table: {error}")
            session.rollback()
    
    commit_and_close()

def getGenerations():
    generations: Generation = get_all_from_table(Generation)
    result = []
    for generation in generations:

        gen = {"id": generation.id,
               "name": generation.name,
               "start_year": generation.start_year,
               "end_year": generation.end_year,
               "is_supported:": isSupported(generation.name),
               "type_chart_id:": generation.type_chart_id}
        result.append(gen)

    return result

def getGenByShortName(gen: PmGen):
    try:
        generation = session.query(Generation).filter_by(name=gen.value).first()
        return generation
    except Exception as e:
        print(f"Error contacting generation table: {e}")
        session.rollback()