from typing import Union
from datetime import date
from sqlalchemy import String, Integer, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pmgens.pmgen import PmGen
from pmgens.generations import Generation, getGenByShortName
from pmalchemy.alchemy import Base, session, get_all_from_table, commit_and_close, get_or_create
from migrations.initialize import games_dict

class PmGame(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    launch_date: Mapped[date] = mapped_column(Date)
    generation_id: Mapped[int] = mapped_column(Integer, ForeignKey("generation.id"))

    generation: Mapped[Generation] = relationship(
        'Generation', foreign_keys=[generation_id], backref='games')

    def __init__(self, name: str, generation: Generation, launch_date: date):
        self.name = name
        self.launch_date = launch_date
        self.generation = generation
        self.generation_id = generation.id
    
    def __str__(self):
            return f"{self.name}"
    
### Functions used in table setup    

def get_game_table():
    generations = get_all_from_table(Generation)
    generation_dict = {gen.name: gen for gen in generations}

    for game_name, game_data in games_dict.items():
        game_name = "Pokémon" + " " + game_name
        generation = generation_dict[game_data["generation"]]
        launch_date = game_data["launch_date"]
        get_or_create(PmGame, name = game_name, generation=generation, launch_date=launch_date)

    commit_and_close()
    print("Game table ready")

### Functions using games

def get_games(gen: Union[PmGen, None] = None):
    if gen == None:
        return get_all_from_table(PmGame)
    elif isinstance(gen, PmGen):
        generation = getGenByShortName(gen)
        return session.query(PmGame).filter_by(generation=generation).all()
