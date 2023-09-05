defaultTypes = {
    "normal": {
        "weak_to": ["fighting"], 
        "resists": [None], 
        "immune_to": ["ghost"]
    },
    "fire": {
        "weak_to": ["water", "ground", "rock"], 
        "resists": ["fire", "grass", "bug"], 
        "immune_to": [None]
    },
    "water": {
        "weak_to": ["electric", "grass"], 
        "resists": ["fire", "water", "ice"], 
        "immune_to": [None]
    },
    "electric": {
        "weak_to": ["ground"], 
        "resists": ["electric", "flying"], 
        "immune_to": [None]
    },
    "grass": {
        "weak_to": ["fire", "ice", "poison", "flying", "bug"], 
        "resists": ["water", "electric", "grass", "ground"], 
        "immune_to": [None]
    },
    "ice": {
        "weak_to": ["fire", "fighting", "rock"], 
        "resists": ["ice"], 
        "immune_to": [None]
    },
    "fighting": {
        "weak_to": ["flying", "psychic"], 
        "resists": ["bug", "rock"], 
        "immune_to": [None]
    },
    "poison": {
        "weak_to": ["ground", "psychic", "bug"], 
        "resists": ["grass", "fighting", "poison"], 
        "immune_to": [None]
    },
    "ground": {
        "weak_to": ["water", "grass", "ice"], 
        "resists": ["poison", "rock"], 
        "immune_to": ["electric"]
    },
    "flying": {
        "weak_to": ["electric", "ice", "rock"], 
        "resists": ["grass", "fighting", "bug"], 
        "immune_to": ["ground"]
    },
    "psychic": {
        "weak_to": ["bug"], 
        "resists": ["fighting", "psychic"], 
        "immune_to": ["ghost"] 
    },
    "bug": {
        "weak_to": ["fire", "flying", "rock"], 
        "resists": ["grass", "fighting", "ground"], 
        "immune_to": [None]
    },
    "rock": {
        "weak_to": ["water", "grass", "fighting", "ground"], 
        "resists": ["normal", "fire", "poison", "flying"], 
        "immune_to": [None]
    },
    "ghost": {
        "weak_to": ["ghost"], 
        "resists": ["poison", "bug"], 
        "immune_to": ["normal", "fighting"]
    },
    "dragon": {
        "weak_to": ["ice", "dragon"], 
        "resists": ["fire", "water", "electric", "grass"], 
        "immune_to": [None]
    }
}

gen2To5Changes = {
    "fire": {
        "weak_to": ["water", "ground", "rock"], 
        "resists": ["fire", "grass", "bug", "steel"], 
        "immune_to": [None]
    },
    "water": {
        "weak_to": ["electric", "grass"], 
        "resists": ["fire", "water", "ice", "steel"], 
        "immune_to": [None]
    },
    "electric": {
        "weak_to": ["ground"], 
        "resists": ["electric", "flying", "steel"], 
        "immune_to": [None]
    },
    "ice": {
        "weak_to": ["fire", "fighting", "rock", "steel"], 
        "resists": ["ice"], 
        "immune_to": [None]
    },
    "fighting": {
        "weak_to": ["flying", "psychic"], 
        "resists": ["bug", "rock", "dark"], 
        "immune_to": [None]
    },
    "poison": {
        "weak_to": ["ground", "psychic"], 
        "resists": ["grass", "fighting", "poison", "bug"], 
        "immune_to": [None]
    },
    "psychic": {
        "weak_to": ["bug", "ghost", "dark"], 
        "resists": ["fighting", "psychic"], 
        "immune_to": [None]
    },
    "bug": {
        "weak_to": ["fire", "flying", "rock"], 
        "resists": ["grass", "fighting", "ground"], 
        "immune_to": [None]
    },
    "rock": {
        "weak_to": ["water", "grass", "fighting", "ground", "steel"], 
        "resists": ["normal", "fire", "poison", "flying"], 
        "immune_to": [None]
    },
    "ghost": {
        "weak_to": ["ghost", "dark"], 
        "resists": ["poison", "bug"], 
        "immune_to": ["normal", "fighting"]
    },
    "dark": {
        "weak_to": ["fighting", "bug"],
        "resists": ["ghost", "dark"], 
        "immune_to": ["psychic"]
    },
    "steel": {
        "weak_to": ["fire", "fighting", "ground"], 
        "resists": ["normal", "grass", "ice", "flying",
                     "psychic", "bug", "rock", "ghost",
                       "dragon", "dark", "steel"], 
        "immune_to": ["poison"]
    },
}

gen6ToCurrentChanges = {
    "fire": {
        "weak_to": ["water", "ground", "rock"], 
        "resists": ["fire", "grass", "bug", "steel", "fairy"], 
        "immune_to": [None]
    },
    "fighting": {
        "weak_to": ["flying", "psychic", "fairy"], 
        "resists": ["bug", "rock", "dark"], 
        "immune_to": [None]
    },
    "poison": {
        "weak_to": ["ground", "psychic"], 
        "resists": ["grass", "fighting", "poison", "bug", "fairy"], 
        "immune_to": [None]
    },
    "dragon": {
        "weak_to": ["ice", "dragon", "fairy"], 
        "resists": ["fire", "water", "electric", "grass"], 
        "immune_to": [None]
    },
    "dark": {
        "weak_to": ["fighting", "bug", "fairy"], 
        "resists": ["ghost", "dark"], 
        "immune_to": ["psychic"]
    },
    "steel": {
        "weak_to": ["fire", "fighting", "ground"], 
        "resists": ["normal", "grass", "ice",
                     "flying", "psychic", "bug",
                       "rock", "dragon", "steel", "fairy"], 
        "immune_to": ["poison"]
    },
    "fairy": {
        "weak_to": ["poison", "steel"], 
        "resists": ["fighting", "bug", "dark"], 
        "immune_to": ["dragon"]
    }
}
