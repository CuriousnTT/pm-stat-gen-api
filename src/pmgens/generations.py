from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.pmalchemy.alchemy import Base, session, commit_and_close, get_all_from_table
from src.migrations.initialize import generations
from src.pmgens.pmgen import PmGen, is_supported

class Generation(Base):
    __tablename__ = "generation"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(5), unique=True)
    start_year: Mapped[int] = mapped_column(Integer)
    end_year: Mapped[int] = mapped_column(Integer, nullable=True)
    game_code: Mapped[str] = mapped_column(String(5), unique=True)
    type_chart_id: Mapped[int] = mapped_column(Integer, ForeignKey('type_charts.id'))

    def __init__(self, id: int, name: str, start_year: int, end_year: int, game_code: str, pm_type_chart_id: int):
        self.id = id
        self.name = name
        self.start_year = start_year
        self.end_year = end_year
        self.game_code = game_code
        self.type_chart_id = pm_type_chart_id
    
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.name
    

    
def get_generations_table():
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
                    game_code=gen_dict["game_code"],
                    pm_type_chart_id=gen_dict["type_chart"]
                    )
                session.add(generation)
        except Exception as error:
            print(f"Error adding generation to table: {error}")
            session.rollback()
    
    commit_and_close()
    print("Generation table ready")

def getGenerations():
    generations: Generation = get_all_from_table(Generation)
    result = []
    for generation in generations:

        gen = {"id": generation.id,
               "name": generation.name,
               "start_year": generation.start_year,
               "end_year": generation.end_year,
               "game_code": generation.game_code,
               "is_supported:": is_supported(generation.name),
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