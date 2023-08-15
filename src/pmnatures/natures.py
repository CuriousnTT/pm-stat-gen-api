from enum import Enum
from typing import Union
import random

from pmstats.basestats import Atk, Def, SpA, SpD, Spe, BaseStat

class NatureRelevantStat(Enum):
    Atk = Atk.abrv
    Def = Def.abrv
    SpA = SpA.abrv
    SpD = SpD.abrv
    Spe = Spe.abrv

class PmNature():
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
    
    def __repr__(self):
        return {"name": {self.name},
                "boosts": {self.boosts},
                "reduces": {self.reduces}}

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