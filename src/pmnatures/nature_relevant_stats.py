from enum import Enum
from src.pmalchemy.alchemy import session
from src.migrations.initialize import stats

irrelevant_stats = [
    "hit points",
    "special",
]

class NatureRelevantStat(Enum):
    pass

NatureRelevantStat = Enum("NatureRelevantStat", [(stat, stat) for stat in stats if stat not in irrelevant_stats])