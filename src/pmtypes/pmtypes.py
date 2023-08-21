from pmgens.genenum import PmGen

class PmType:
    def __init__(self, name: str , weakTo, resists, immuneTo):
        self.name = name
        self.weakTo = weakTo
        self.resists = resists
        self.immuneTo = immuneTo

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return {"name": {self.name},
                "weakTo": {self.weakTo},
                "resists": {self.resists},
                "immuneTo": {self.immuneTo}
            }
    
#Default is intended generation 1
defaultTypes = {
    "normal": {
        "weakTo": ["fighting"], "resists": [None], "immuneTo": ["ghost"]
    },
    "fire": {"weakTo": ["water", "ground", "rock"], "resists": ["fire", "grass", "bug"], "immuneTo": [None]
    },
    "water": {
        "weakTo": ["electric", "grass"], "resists": ["fire", "water", "ice"], "immuneTo": [None]
    },
    "electric": {
        "weakTo": ["ground"], "resists": ["electric", "flying"], "immuneTo": [None]
    },
    "grass": {
        "weakTo": ["fire", "ice", "poison", "flying", "bug"], "resists": ["water", "electric", "grass", "ground"], "immuneTo": [None]
    },
    "ice": {
        "weakTo": ["fire", "fighting", "rock"], "resists": ["ice"], "immuneTo": [None]
    },
    "fighting": {
        "weakTo": ["flying", "psychic"], "resists": ["bug", "rock"], "immuneTo": [None]
    },
    "poison": {
        "weakTo": ["ground", "psychic"], "resists": ["grass", "fighting", "poison", "bug"], "immuneTo": [None]
    },
    "ground": {
        "weakTo": ["water", "grass", "ice"], "resists": ["poison", "rock"], "immuneTo": ["electric"]
    },
    "flying": {
        "weakTo": ["electric", "ice", "rock"], "resists": ["grass", "fighting", "bug"], "immuneTo": ["ground"]
    },
    "psychic": {
        "weakTo": ["bug", "ghost"], "resists": ["fighting", "psychic"], "immuneTo": [None]
    },
    "bug": {
        "weakTo": ["fire", "flying", "rock"], "resists": ["grass", "fighting", "ground"], "immuneTo": [None]
    },
    "rock": {
        "weakTo": ["water", "grass", "fighting", "ground"], "resists": ["normal", "fire", "poison", "flying"], "immuneTo": [None]
    },
    "ghost": {
        "weakTo": ["ghost"], "resists": ["poison", "bug"], "immuneTo": ["normal", "fighting"]
    },
    "dragon": {
        "weakTo": ["ice", "dragon"], "resists": ["fire", "water", "electric", "grass"], "immuneTo": [None]
    }
}

gen1Quirks = {
    "poison": {
        "weakTo": ["ground", "psychic", "bug"], "resists": ["grass", "fighting", "poison"], "immuneTo": [None]
    },
    "psychic": {
        "weakTo": ["bug"], "resists": ["fighting", "psychic"], "immuneTo": ["ghost"] 
    },
    "bug": {
        "weakTo": ["fire", "flying", "poison", "rock"], "resists": ["grass", "fighting", "ground"], "immuneTo": [None]
    },
}

gen2To5Changes = {
    "fire": {"weakTo": ["water", "ground", "rock"], "resists": ["fire", "grass", "bug", "steel"], "immuneTo": [None]
    },
    "water": {
        "weakTo": ["electric", "grass"], "resists": ["fire", "water", "ice", "steel"], "immuneTo": [None]
    },
    "electric": {
        "weakTo": ["ground"], "resists": ["electric", "flying", "steel"], "immuneTo": [None]
    },
    "ice": {
        "weakTo": ["fire", "fighting", "rock", "steel"], "resists": ["ice"], "immuneTo": [None]
    },
    "fighting": {
        "weakTo": ["flying", "psychic"], "resists": ["bug", "rock", "dark"], "immuneTo": [None]
    },
    "psychic": {
        "weakTo": ["bug", "ghost", "dark"], "resists": ["fighting", "psychic"], "immuneTo": [None]
    },
    "rock": {
        "weakTo": ["water", "grass", "fighting", "ground", "steel"], "resists": ["normal", "fire", "poison", "flying"], "immuneTo": [None]
    },
    "ghost": {
        "weakTo": ["ghost", "dark"], "resists": ["poison", "bug"], "immuneTo": ["normal", "fighting"]
    },
    "dark": {
        "weakTo": ["fighting", "bug"], "resists": ["ghost", "dark"], "immuneTo": ["psychic"]
    },
    "steel": {
        "weakTo": ["fire", "fighting", "ground"], "resists": ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel"], "immuneTo": ["poison"]
    },
}

gen6ToCurrentChanges = {
    "fire": {
        "weakTo": ["water", "ground", "rock"], "resists": ["fire", "grass", "bug", "steel", "fairy"], "immuneTo": [None]
    },
    "fighting": {
        "weakTo": ["flying", "psychic", "fairy"], "resists": ["bug", "rock", "dark"], "immuneTo": [None]
    },
    "poison": {
        "weakTo": ["ground", "psychic"], "resists": ["grass", "fighting", "poison", "bug", "fairy"], "immuneTo": [None]
    },
    "dragon": {
        "weakTo": ["ice", "dragon", "fairy"], "resists": ["fire", "water", "electric", "grass"], "immuneTo": [None]
    },
    "dark": {
        "weakTo": ["fighting", "bug", "fairy"], "resists": ["ghost", "dark"], "immuneTo": ["psychic"]
    },
    "steel": {
        "weakTo": ["fire", "fighting", "ground"], "resists": ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "dragon", "steel", "fairy"], "immuneTo": ["poison"]
    },
    "fairy": {
        "weakTo": ["poison", "steel"], "resists": ["fighting", "bug", "dark"], "immuneTo": ["dragon"]
    }
}

def createPmTypes(gen: PmGen, intended: bool = False):
    properties = defaultTypes.copy()

    if gen != PmGen.GEN1:
        properties.update(gen2To5Changes)
        if gen not in [PmGen.GEN2, PmGen.GEN3, PmGen.GEN4, PmGen.GEN5]:
            properties.update(gen6ToCurrentChanges)
    elif intended == False:
        properties.update(gen1Quirks)
    
    types = []

    for name in properties:
        typeProperties = properties[name]
        typeProperties["name"] = name
        types.append(PmType(**typeProperties))

    return types