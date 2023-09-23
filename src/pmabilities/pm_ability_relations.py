from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.pmalchemy.alchemy import Base

class PmAbilities(Base):
    __tablename__ = 'pm_abilities'

    
