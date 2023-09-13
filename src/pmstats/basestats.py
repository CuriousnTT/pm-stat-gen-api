from src.pmgens.pmgen import PmGen
from typing import Union

class BaseStat:
    def __init__(self, name, short_name):
        self.name = name
        self.short_name = short_name

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.short_name}"
    
HP = BaseStat("Hit Points", "HP")
Atk = BaseStat("Attack", "Atk")
Def = BaseStat("Defense", "Def")
Spc = BaseStat("Special", "Spc")
SpA = BaseStat("Special Attack", "SpA")
SpD = BaseStat("Special Defense", "SpD")
Spe = BaseStat("Speed", "Spe")

def getBaseStats(gen: Union[PmGen, None] = None):
    baseStats = {HP, Atk, Def, SpA, SpD, Spe}
    if gen == None:
        genValue = "2 and later"
    else:
        genValue = gen.value
        if gen == PmGen.GEN1:
            baseStats = {HP, Atk, Def, Spc, Spe}
    baseStatsInfo = {"info": f"There are {len(baseStats)} stats which impact combat in {genValue}. Valid pokemon have a value for each.",
                 "length": len(baseStats),
                 "Base Stats": baseStats}
    return baseStatsInfo