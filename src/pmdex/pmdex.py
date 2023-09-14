from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pmalchemy.alchemy import Base, session
from pmdex.evolutions import EvolutionStage

class PmDex(Base):
    __tablename__='pmdex'

    nat_dex_nr: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)
    dex_header: Mapped[str] = mapped_column(String(45))
    evolution_stage_id: Mapped[int] = mapped_column(Integer, ForeignKey('evolution_stage.id'))
    evolution_stage: Mapped[EvolutionStage] = relationship('EvolutionStage', foreign_keys=[evolution_stage_id])

    def __init__(self, nat_dex_nr: int, name: str, dex_header: str, evolution_stage: EvolutionStage):
        self.nat_dex_nr = nat_dex_nr
        self.name = name
        self.dex_header = dex_header
        self.evolution_stage_id = evolution_stage.id
        self.evolution_stage = evolution_stage