from enum import Enum

class Constants(Enum):
    CURRENTDATASETTYPES = ["xlsx"]
    DESIREDCOLUMNS = [ #potentially move this to csv/json file
    "Pokemon", "Level", 
    "Type 1", "Type 2", 
    "Move 1", "Move 2", "Move 3", "Move 4",
    "HP Stat", "Attack Stat", "Defense Stat", "Special Stat", "Special Attack Stat", "Special Defense Stat", "Speed Stat",
    "Attack DV", "Defense DV", "Special DV", "Speed DV",
    "HP IV", "Attack IV", "Defense IV", "Special Attack IV", "Special Defense IV", "Speed IV",
    "HP Stat Experience", "Attack Stat Experience", "Defense Stat Experience", "Special Stat Experience" "Special Attack Stat Experience", "Special Defense Stat Experience", "Speed Stat Experience",
    "HP EV", "Attack EV", "Defense EV", "Special Attack EV", "Special Defense EV", "Speed EV"
]