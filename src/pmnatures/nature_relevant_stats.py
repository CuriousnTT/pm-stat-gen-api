from enum import Enum
from src.pmalchemy.alchemy import session
from src.pmstats.basestats import Stat

irrelevant_stats = [
    "hit points",
    "special",
]

class NatureRelevantStat(Enum):
    pass

stats = session.query(Stat).filter(Stat.name.not_in(irrelevant_stats)).all()

NatureRelevantStat = Enum("NatureRelevantStat", [(stat.name, stat.name) for stat in stats])