from typing import Union
from sqlalchemy import Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.pmalchemy.alchemy import Base
from src.pmgens.generations import Generation
from src.pmtypes.pmtypes import PmType
from src.pmdex.pmforms import PmForm

class PmSpecifics(Base):
    __tablename__ = 'pm_specifics'

    gen_id: Mapped[int] = mapped_column(Integer, ForeignKey('generation.id'))
    primary_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('types.id'))
    secondary_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('types.id'))
    ability_id: Mapped[int] = mapped_column(Integer, ForeignKey('ability.id'), nullable=True)
    form_id: Mapped[int] = mapped_column(Integer, ForeignKey('form.id'))
    male_ratio: Mapped[float] = mapped_column(Float)

    def __init__(self, generation: Generation, primary_type: PmType, secondary_type: PmType, form: PmForm, male_ratio: float):
        self.gen_id = generation.id
        self.primary_type_id = primary_type.id
        self.secondary_type_id = secondary_type.id
        self.ability = ability        