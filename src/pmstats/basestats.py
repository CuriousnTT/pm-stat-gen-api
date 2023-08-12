class BaseStat:
    def __init__(self, name, abbreviation):
        self.name = name
        self.abrv = abbreviation

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.abrv}"
    
HP = BaseStat("Hit Points", "HP")
Atk = BaseStat("Attack", "Atk")
Def = BaseStat("Defense", "Def")
Spc = BaseStat("Special", "Spc")
SpA = BaseStat("Special Attack", "SpA")
SpD = BaseStat("Special Defense", "SpD")
Spe = BaseStat("Speed", "Spe")

def getBaseStats(gen = None):
    if gen == "gen1":
        baseStats = {HP, Atk, Def, Spc, Spe}
        genValue = "generation 1"
    else:
        baseStats = {HP, Atk, Def, SpA, SpD, Spe}
        genValue = "generations 2 and later"
    baseStatsInfo = {"info": f"There are {len(baseStats)} stats which impact combat in {genValue}. Valid pokemon have a value for each.",
                     "length": len(baseStats),
                     "Base Stats": baseStats}
    return baseStatsInfo