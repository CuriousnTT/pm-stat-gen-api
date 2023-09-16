import enum
import random
from typing import Union
from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column
from src.pmalchemy.alchemy import Base
from src.pmstats.basestats import Atk, Def, SpA, SpD, Spe

class NatureRelevantStat(enum.Enum):
    Atk = Atk.short_name
    Def = Def.short_name
    SpA = SpA.short_name
    SpD = SpD.short_name
    Spe = Spe.short_name

class PmNature(Base):
    __tablename__ = "pm_nature"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    boosts: Mapped[Enum] = mapped_column(Enum(NatureRelevantStat), nullable=True)
    reduces: Mapped[Enum] = mapped_column(Enum(NatureRelevantStat), nullable=True)

    def __init__(self, name: str, boosts: Union[NatureRelevantStat, None] = None, reduces: Union[NatureRelevantStat, None] = None):
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

hardy = PmNature("Hardy")
lonely = PmNature("Lonely", NatureRelevantStat.Atk, NatureRelevantStat.Def)
adamant = PmNature("Adamant", NatureRelevantStat.Atk, NatureRelevantStat.SpA)
naughty = PmNature("Naughty", NatureRelevantStat.Atk, NatureRelevantStat.SpD)
brave = PmNature("Brave", NatureRelevantStat.Atk, NatureRelevantStat.Spe)
bold = PmNature("Bold", NatureRelevantStat.Def, NatureRelevantStat.Atk)
docile = PmNature("Docile")
impish = PmNature("Impish", NatureRelevantStat.Def, NatureRelevantStat.SpA)
lax = PmNature("Lax", NatureRelevantStat.Def, NatureRelevantStat.SpD)
relaxed = PmNature("Relaxed", NatureRelevantStat.Def, NatureRelevantStat.Spe)
modest = PmNature("Modest", NatureRelevantStat.SpA, NatureRelevantStat.Atk)
mild = PmNature("Mild", NatureRelevantStat.SpA, NatureRelevantStat.Def)
bashful = PmNature("Bashful")
rash = PmNature("Rash", NatureRelevantStat.SpA, NatureRelevantStat.SpD)
quiet = PmNature("Quiet", NatureRelevantStat.SpA, NatureRelevantStat.Spe)
calm = PmNature("Calm", NatureRelevantStat.SpD, NatureRelevantStat.Atk)
gentle = PmNature("Gentle", NatureRelevantStat.SpD, NatureRelevantStat.Def)
careful = PmNature("Careful", NatureRelevantStat.SpD, NatureRelevantStat.SpA)
quirky = PmNature("Quirky")
sassy = PmNature("Sassy", NatureRelevantStat.SpD, NatureRelevantStat.Spe)
timid = PmNature("Timid", NatureRelevantStat.Spe, NatureRelevantStat.Atk)
hasty = PmNature("Hasty", NatureRelevantStat.Spe, NatureRelevantStat.Def)
jolly = PmNature("Jolly", NatureRelevantStat.Spe, NatureRelevantStat.SpA)
naive = PmNature("Naive", NatureRelevantStat.Spe, NatureRelevantStat.SpD)
serious = PmNature("Serious")

naturesList = [hardy, lonely, adamant, naughty, brave, bold, docile, impish, lax, relaxed, modest, mild, bashful, rash, quiet, calm, gentle, careful, quirky, sassy, timid, hasty, jolly, naive, serious]


def getNature():
    return random.choice(naturesList)

def getSpecificNatures(stat: NatureRelevantStat, boosts: bool):
    specificNatures = []
    if boosts == True:
        for x in naturesList:
            if x.boosts == stat:
                specificNatures.append(x)
    elif boosts == False:
        for x in naturesList:
            if x.reduces == stat:
                specificNatures.append(x)
    return specificNatures