from datetime import date
from pmgens.pmgen import PmGen

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
    },
    "unknown": {
        "weak_to": [None],
        "resists": [None],
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

generations = {
    "gen1": {
        "start_year": 1996,
        "end_year": 1999,
        "game_code": "RBY",
        "type_chart": 1
    },
    "gen2": {
        "start_year": 1999,
        "end_year": 2002,
        "game_code": "GSC",
        "type_chart": 2
    },
    "gen3": {
        "start_year": 2002,
        "end_year": 2006,
        "game_code": "RSE",
        "type_chart": 2
    },
    "gen4": {
        "start_year": 2006,
        "end_year": 2010,
        "game_code": "DPPt",
        "type_chart": 2
    },
    "gen5": {
        "start_year": 2010,
        "end_year": 2013,
        "game_code": "BW",
        "type_chart": 2
    },
    "gen6": {
        "start_year": 2013,
        "end_year": 2016,
        "game_code": "XY",
        "type_chart": 3
    },
    "gen7": {
        "start_year": 2016,
        "end_year": 2019,
        "game_code": "SM",
        "type_chart": 3
    },
    "gen8": {
        "start_year": 2019,
        "end_year": 2023,
        "game_code": "SS",
        "type_chart": 3
    },
    "gen9": {
        "start_year": 2022,
        "end_year": None,
        "game_code": "SV",
        "type_chart": 3
    }
}

games_dict = {
    "Red": {
        "launch_date": date(1996, 2, 27),
        "generation": PmGen.GEN1.value     
    },
    "Green": {
        "launch_date": date(1996, 2, 27),
        "generation": PmGen.GEN1.value
    },
    "Blue": {
        "launch_date": date(1996, 10, 15),
        "generation": PmGen.GEN1.value
    },
    "Yellow": {
        "launch_date": date(1998, 9, 12),
        "generation": PmGen.GEN1.value
    },
    "Gold": {
        "launch_date": date(1999, 11, 21),
        "generation": PmGen.GEN2.value
    },
    "Silver": {
        "launch_date": date(1999, 11, 21),
        "generation": PmGen.GEN2.value
    },
    "Crystal": {
        "launch_date": date(2000, 12, 14),
        "generation": PmGen.GEN2.value
    },
    "Ruby": {
        "launch_date": date(2002, 11, 21),
        "generation": PmGen.GEN3.value
    },
    "Sapphire": {
        "launch_date": date(2002, 11, 21),
        "generation": PmGen.GEN3.value
    },
    "FireRed": {
        "launch_date": date(2004, 1, 29),
        "generation": PmGen.GEN3.value
    },
    "LeafGreen": {
        "launch_date": date(2004, 1, 29),
        "generation": PmGen.GEN3.value
    },
    "Emerald": {
        "launch_date": date(2004, 9, 11),
        "generation": PmGen.GEN3.value
    },
    "Diamond": {
        "launch_date": date(2006, 9, 28),
        "generation": PmGen.GEN4.value
    },
    "Pearl": {
        "launch_date": date(2006, 9, 28),
        "generation": PmGen.GEN4.value
    },
    "Platinum": {
        "launch_date": date(2008, 9, 13),
        "generation": PmGen.GEN4.value
    },
    "HeartGold": {
        "launch_date": date(2009, 9, 12),
        "generation": PmGen.GEN4.value
    },
    "SoulSilver": {
        "launch_date": date(2009, 9, 12),
        "generation": PmGen.GEN4.value
    },
    "Black": {
        "launch_date": date(2010, 9, 18),
        "generation": PmGen.GEN5.value
    },
    "White": {
        "launch_date": date(2010, 9, 18),
        "generation": PmGen.GEN5.value
    },
    "Black 2": {
        "launch_date": date(2012, 6, 23),
        "generation": PmGen.GEN5.value
    },
    "White 2": {
        "launch_date": date(2010, 6, 23),
        "generation": PmGen.GEN5.value
    },
    "X": {
        "launch_date": date(2013, 10, 12),
        "generation": PmGen.GEN6.value
    },
    "Y": {
        "launch_date": date(2013, 10, 12),
        "generation": PmGen.GEN6.value
    },
    "Omega Ruby": {
        "launch_date": date(2014, 11, 21),
        "generation": PmGen.GEN6.value
    },
    "Alpha Sapphire": {
        "launch_date": date(2014, 11, 21),
        "generation": PmGen.GEN6.value
    },
    "Sun": {
        "launch_date": date(2016, 11, 17),
        "generation": PmGen.GEN7.value
    },
    "Moon": {
        "launch_date": date(2016, 11, 17),
        "generation": PmGen.GEN7.value
    },
    "Ultra Sun": {
        "launch_date": date(2017, 11, 17),
        "generation": PmGen.GEN7.value
    },
    "Ultra Moon": {
        "launch_date": date(2017, 11, 17),
        "generation": PmGen.GEN7.value
    },
    "Let's Go Pikachu!": {
        "launch_date": date(2018, 11, 16),
        "generation": PmGen.GEN7.value
    },
    "Let's Go Eevee!": {
        "launch_date": date(2018, 11, 16),
        "generation": PmGen.GEN7.value
    },
    "Sword": {
        "launch_date": date(2019, 11, 15),
        "generation": PmGen.GEN8.value
    },
    "Shield": {
        "launch_date": date(2019, 11, 15),
        "generation": PmGen.GEN8.value
    },
    "Brilliant Diamond": {
        "launch_date": date(2021, 11, 19),
        "generation": PmGen.GEN8.value
    },
    "Shining Pearl": {
        "launch_date": date(2021, 11, 19),
        "generation": PmGen.GEN8.value
    },
    "Legends: Arceus": {
        "launch_date": date(2022, 1, 28),
        "generation": PmGen.GEN8.value
    },
    "Scarlet": {
        "launch_date": date(2023, 11, 18),
        "generation": PmGen.GEN9.value
    },
    "Violet": {
        "launch_date": date(2023, 11, 18),
        "generation": PmGen.GEN9.value
    },
}