from enum import Enum
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from pmalchemy.alchemy import Base, session, commit_and_close, get_all_from_table

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
    type_chart_id: Mapped[int] = mapped_column(Integer, ForeignKey('type_charts.id'))

    def __init__(self, name: str, short_name: str, pm_type_chart_id: int):
        self.name = name
        self.short_name = short_name
        self.type_chart_id = pm_type_chart_id
    
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.short_name
    
def isSupported(gen: PmGen):
        if gen in list(SupportedGen):
            return True
        else:
            return False
    
def getGenerationsTable():
    id = 0
    gen_one_chart, gen_two_to_five_chart, gen_six_to_current_chart = [
    1, 2, 3]
    for x in list(PmGen):
        id += 1
        name = f"generation {id}"
        if id == 1:
            type_chart = gen_one_chart
        elif id in [2, 3, 4, 5]:
            type_chart = gen_two_to_five_chart
        elif id <= 6:
            type_chart = gen_six_to_current_chart
        try:
            generation = session.query(Generation).filter_by(id=id).first()
            if generation is None:
                session.add(Generation(name=name, short_name=x.value, pm_type_chart_id=type_chart))
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
               "short_name": generation.short_name,
               "is_supported:": isSupported(generation.short_name),
               "type_chart_id:": generation.type_chart_id}
        result.append(gen)

    return result

def getGenByShortName(gen: PmGen):
    try:
        generation = session.query(Generation).filter_by(short_name=gen.value).first()
        return generation
    except Exception as e:
        print(f"Error contacting generation table: {e}")
        session.rollback()