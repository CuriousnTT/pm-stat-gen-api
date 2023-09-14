from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from pmalchemy.alchemy import Base, commit_and_close, get_or_create

class EvolutionStage(Base):
    __tablename__ = 'evolution_stage'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[String] = mapped_column(String)

    def __init__(self, name):
        self.id = self.id
        self.name = name

def get_evolution_stage_table():
    stage_names = ["baby", "base", "middle", "final"]
    for name in stage_names:
        get_or_create(
            EvolutionStage,
            name=name,
            )
    commit_and_close()
    print("Evolution Stage table ready")