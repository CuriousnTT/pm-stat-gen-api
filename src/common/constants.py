#doesn't work sadly :(, constants expected to only be used at modular level, meaning we gonna have some duplicate constants
class Constants:
    CURRENTDATASETTYPES = ["xlsx"]
    DESIREDCOLUMNS = [ #potentially move this to csv/json file
    "Pokemon", "Level", 
    "Type 1", "Type 2", 
    "Move 1", "Move 2", "Move 3", "Move 4",
    "HP Stat", "Attack Stat", "Defense Stat", "Special Stat", "Special Attack Stat", "Special Defense Stat", "Speed Stat",
    "Attack DV", "Defense DV", "Special DV", "Speed DV",
    "HP IV", "Attack IV", "Defense IV", "Special Attack IV", "Special Defense IV", "Speed IV"
]