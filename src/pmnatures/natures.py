from typing import Union

from pmstats.basestats import Atk, Def, SpA, SpD, Spe

class PmNature():
    def __init__(self, name: str, boosts: Union[Atk, Def, SpA, SpD, Spe, None] = None, reduces: Union[Atk, Def, SpA, SpD, Spe, None] = None):
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