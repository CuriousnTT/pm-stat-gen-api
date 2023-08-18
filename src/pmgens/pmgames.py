from typing import Union
from pmgens.genenum import PmGen
from pmgens.genenum import isSupported
from sqlalchemy import String, Column, Integer, Enum
from pmalchemy.alchemy import Base


class PmGame(Base):
    __tablename__ = "pm_game"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gen = Column(Enum(PmGen))
    remake = Column(Integer)

    def __init__(self, name: str, gen: PmGen, remake: bool = False):
        self.name = name
        self.gen = gen
        self.remake = remake
    
    def __repr__(self):
        return {"name": {self.name},
                "generation": {self.gen},
                "remake": {self.remake}
                }
    
    def __str__(self):
        if self.remake:
            return f"{self.name} is a remake from {self.gen}"
        else:
            return f"{self.name} from {self.gen}"
    
red = PmGame("Red", "gen1")
blue = PmGame("Blue", "gen1")
yellow = PmGame("Yellow", "gen1")
gold = PmGame("Gold", "gen2")
silver = PmGame("Silver", "gen2")
crystal = PmGame("Crystal", "gen2")
ruby = PmGame("Ruby", "gen3")
sapphire = PmGame("Sapphire", "gen3")
emerald = PmGame("Emerald", "gen3")
fireRed = PmGame("FireRed", "gen3", True)
leafGreen = PmGame("LeafGreen", "gen3", True)
diamond = PmGame("Diamond", "gen4")
pearl = PmGame("Pearl", "gen4")
platinum = PmGame("Platinum", "gen4")
heartGold = PmGame("HeartGold", "gen4", True)
soulSilver = PmGame("SoulSilver", "gen4", True)
black = PmGame("Black", "gen5")
white = PmGame("White", "gen5")
black2 = PmGame("Black 2", "gen5")
white2 = PmGame("White 2", "gen5")
pmX = PmGame("X", "gen6")
pmY = PmGame("Y", "gen6")
alphaSapphire = PmGame("AlphaSapphire", "gen6", True)
omegaRuby = PmGame("OmegaRuby", "gen6", True)
sun = PmGame("Sun", "gen7")
moon = PmGame("Moon", "gen7")
ultraSun = PmGame("UltraSun", "gen7", True)
ultraMoon = PmGame("UltraMoon", "gen7", True)
letsGoEevee = PmGame("Let's Go Eevee", "gen7", True)
letsGoPikachu = PmGame("Let's Go Pikachu", "gen7", True)
sword = PmGame("Sword", "gen8")
shield = PmGame("Shield", "gen8")
brilliantDiamond = PmGame("Brilliant Diamond", "gen8", True)
shiningPearl = PmGame("Shining Pearl", "gen8", True)
legendsArceus = PmGame("Legends Arceus", "gen8")
scarlet = PmGame("Scarlet", "gen9")
violet = PmGame("Violet", "gen9")

games = {
    PmGen.GEN1: {
        "games": {red, blue, yellow},
        "remakes": None,
        "code": "RBY",
        "supported": isSupported(PmGen.GEN1)},
    PmGen.GEN2: {"games": {gold, silver, crystal},
        "remakes": None,
        "code": "GSC",
        "supported": isSupported(PmGen.GEN2)},
    PmGen.GEN3: {"games": {ruby, sapphire, emerald},
        "remakes": {fireRed, leafGreen},
        "code": "RSE",
        "supported": isSupported(PmGen.GEN3)},
    PmGen.GEN4: {"games": {diamond, pearl, platinum},
        "remakes": {heartGold, soulSilver},
        "code": "DPPt",
        "supported": isSupported(PmGen.GEN4)},
    PmGen.GEN5: {"games": {black, white, black2, white2},
        "remakes": None,
        "code": "BW",
        "supported": isSupported(PmGen.GEN5)},
    PmGen.GEN6: {"games": {pmX, pmY},
        "remakes": {alphaSapphire, omegaRuby},
        "code": "XY",
        "supported": isSupported(PmGen.GEN6)},
    PmGen.GEN7: {"games": {sun, moon},
        "remakes": {ultraSun, ultraMoon, letsGoEevee, letsGoPikachu},
        "code": "SM",
        "supported": isSupported(PmGen.GEN7)},
    PmGen.GEN8: {"games": {sword, shield, legendsArceus},
        "remakes": {brilliantDiamond, shiningPearl},
        "code": "SS",
        "supported": isSupported(PmGen.GEN8)},
    PmGen.GEN9: {"games": {scarlet, violet},
        "remakes": None,
        "code": "SV",
        "supported": isSupported(PmGen.GEN9)}
}

def getGames(gen: Union[PmGen, None] = None):
    if gen == None:
        return games
    elif isinstance(gen, PmGen):
        return games[gen]
