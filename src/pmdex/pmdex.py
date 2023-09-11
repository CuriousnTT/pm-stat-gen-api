from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pmgens.generations import Generation
from pmtypes.pmtypes import PmType
from pmalchemy.alchemy import Base, session

class PmDex(Base):
    __tablename__='pmdex'

    Dex_nr: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)
    origin_generation_id: Mapped[int] = mapped_column(Integer, ForeignKey('generation.id'))
    origin_generation: Mapped[Generation] = relationship('Generation', foreign_keys=[origin_generation_id], backref='pmdex')
    