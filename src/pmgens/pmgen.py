from enum import Enum

class PmGen(Enum):
    GEN1 = "gen1"
    GEN2 = "gen2"
    GEN3 = "gen3"
    GEN4 = "gen4"
    GEN5 = "gen5"
    GEN6 = "gen6"
    GEN7 = "gen7"
    GEN8 = "gen8"
    GEN9 = "gen9"

class SupportedGen(str, Enum):
    GEN1 = "gen1"

def is_supported(gen: PmGen):
        if gen in list(SupportedGen):
            return True
        else:
            return False