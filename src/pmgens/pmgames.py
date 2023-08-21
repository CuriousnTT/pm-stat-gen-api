from typing import Union
from pmgens.genenum import PmGen
from pmgens.genenum import isSupported
from sqlalchemy import Boolean, String, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column
from pmalchemy.alchemy import Base

class PmGame(Base):
    __tablename__ = "pm_game"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    gen: Mapped[Enum] = mapped_column(Enum(PmGen))
    remake: Mapped[bool] = mapped_column(Boolean)

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
    
red = PmGame("Red", 1)
blue = PmGame("Blue", 1)
yellow = PmGame("Yellow", 1)
gold = PmGame("Gold", 2)
silver = PmGame("Silver", 2)
crystal = PmGame("Crystal", 2)
ruby = PmGame("Ruby", 3)
sapphire = PmGame("Sapphire", 3)
emerald = PmGame("Emerald", 3)
fireRed = PmGame("FireRed", 3, True)
leafGreen = PmGame("LeafGreen", 3, True)
diamond = PmGame("Diamond", 4)
pearl = PmGame("Pearl", 4)
platinum = PmGame("Platinum", 4)
heartGold = PmGame("HeartGold", 4, True)
soulSilver = PmGame("SoulSilver", 4, True)
black = PmGame("Black", 5)
white = PmGame("White", 5)
black2 = PmGame("Black 2", 5)
white2 = PmGame("White 2", 5)
pmX = PmGame("X", 6)
pmY = PmGame("Y", 6)
alphaSapphire = PmGame("AlphaSapphire", 6, True)
omegaRuby = PmGame("OmegaRuby", 6, True)
sun = PmGame("Sun", 7)
moon = PmGame("Moon", 7)
ultraSun = PmGame("UltraSun", 7, True)
ultraMoon = PmGame("UltraMoon", 7, True)
letsGoEevee = PmGame("Let's Go Eevee", 7, True)
letsGoPikachu = PmGame("Let's Go Pikachu", 7, True)
sword = PmGame("Sword", 8)
shield = PmGame("Shield", 8)
brilliantDiamond = PmGame("Brilliant Diamond", 8, True)
shiningPearl = PmGame("Shining Pearl", 8, True)
legendsArceus = PmGame("Legends Arceus", 8)
scarlet = PmGame("Scarlet", 9)
violet = PmGame("Violet", 9)

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
