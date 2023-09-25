import random
from typing import Union
from sqlalchemy import String, Integer, ForeignKey, or_
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.pmalchemy.alchemy import Base, session, get_or_create, commit_and_close
from src.pmnatures.nature_relevant_stats import NatureRelevantStat as NRS
from src.migrations.initialize import nature_details

class PmNature(Base):
    __tablename__ = "nature"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    boosts: Mapped[str] = mapped_column(String, nullable=True)
    reduces: Mapped[str] = mapped_column(String, nullable=True)

    def __init__(self, name: str, boosts: Union[str, None] = None, reduces: Union[str, None] = None):
        self.name = name
        self.boosts = boosts
        self.reduces = reduces

    def __str__(self):
        returnstr = f"A pokemon with a {self.name} nature"
        if self.boosts == None and self.reduces == None:
            returnstr = returnstr + " " + "has no particular strengths or weaknesses to its stats."
        else:
            returnstr = returnstr + " " + f"has better {self.boosts} and worse {self.reduces} than average."
        return returnstr
    
def get_nature_table():
    stats = session.query(Stat).all()
    stat_dict = {stat.name: stat for stat in stats}
    
    for nature in nature_details:
        get_or_create(PmNature, name=nature['name'], boosts=nature['boosts'], reduces=nature['reduces'])
    commit_and_close()
    print("Nature table ready")

def getNature():
    try:
        natures = session.query(PmNature).all()
    except Exception as error:
        print(f"Error contacting nature table: {error}")
    else:
        return random.choice(natures)

def getSpecificNatures(stat: NRS, boosts: bool):
    try:
        results = session.query(PmNature).filter(
            or_(
                PmNature.boosts == stat.value if boosts else None,
                PmNature.reduces == stat.value if not boosts else None
            )
        ).all()
    except Exception as error:
        print(f"Error contacting nature table: {error}")
    else:
        return results