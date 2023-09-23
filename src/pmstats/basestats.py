from typing import Union
from sqlalchemy import Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.pmalchemy.alchemy import Base, get_or_create, commit_and_close, session
from src.pmdex.pmforms import PmForm
from src.pmgens.pmgen import PmGen
from src.migrations.initialize import stats

class Stat(Base):
    __tablename__='stat'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(10), unique=True)

    def __repr__(self):
        return self.name

""" class PmStats(Base):
    __tablename__='pm_basestats'

    gen_id: Mapped[int] = mapped_column(Integer, ForeignKey('generation.id'), primary_key=True)
    form_id: Mapped[int] = mapped_column(Integer, ForeignKey('form.id'), primary_key=True)

    form: Mapped[PmForm] = relationship('PmForm', backref='pm_basestats')
 """
""" class PmStatValue(Base):
    __tablename__='pm_stat_value'

    pm_stats_gen_id: Mapped[int] = mapped_column(Integer, ForeignKey('pm_basestats.gen_id'), primary_key=True)
    pm_stats_form_id: Mapped[int] = mapped_column(Integer, ForeignKey('pm_basestats.form_id'), primary_key=True)
    pm_stats_nat_dex_nr: Mapped[int] = mapped_column(Integer, ForeignKey, primary_key=True)
    stat_id: Mapped[int] = mapped_column(Integer, ForeignKey('stat.id'), primary_key=True)
    value: Mapped[int] = mapped_column(Integer)

    pm_stats: Mapped[PmStats] = relationship('PmStats', foreign_keys=[pm_stats_gen_id, pm_stats_form_id, pm_stats_nat_dex_nr])
    pm_stats: Mapped[Stat] = relationship('Stat', foreign_keys=[stat_id])
 """
def get_stat_table():
    for stat in stats:
        get_or_create(Stat, name=stat)
    commit_and_close()
    print("Stat table ready")

def get_generic_base_stats(gen: Union[PmGen, None] = None):
    gen_one_only = ["special"]
    not_in_gen_one = ["special attack", "special defense"]
    absent_stats = gen_one_only
    if gen == None:
        genValue = "2 and later"
    else:
        genValue = gen.value
        if gen == PmGen.GEN1:
            absent_stats = not_in_gen_one
    try:
        base_stats = session.query(Stat).filter(Stat.name.not_in(absent_stats))
    except Exception as error:
        print(f"Error getting stats from database: {error}")
    else:
        baseStatsInfo = {
            "info":
            f"There are {len(base_stats)} stats which impact combat in {genValue}. Valid pokemon have a value for each.",
            "length": len(base_stats),
            "Base Stats": base_stats}
        return baseStatsInfo