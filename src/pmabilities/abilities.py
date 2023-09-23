from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.pmalchemy.alchemy import Base
from src.pmgens.generations import Generation

class Ability(Base):
    __tablename__='ability'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, Unique=True)
    description: Mapped[str] = mapped_column(String)
    generation: Mapped[Generation] = relationship()