from dataclasses import dataclass
from sqlalchemy import Integer, Boolean, ForeignKey, ForeignKeyConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.pmalchemy.alchemy import Base, commit_and_close, session
from src.pmdex.pmsummary import PmSummary, get_summaries_by_gen
from src.pmabilities.abilities import Ability, get_ability_by_name
from src.pmgens.pmgen import PmGen
from src.common.utils import get_list_of_objects_by_template

@dataclass
class PmHasAbilityData:
    pm_summary: PmSummary
    ability: Ability
    hidden: bool

class PmHasAbility(Base):
    __tablename__ = 'pm_has_ability'

    gen_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    form_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nat_dex_nr: Mapped[int] = mapped_column(Integer, primary_key=True)
    ability_id: Mapped[int] = mapped_column(Integer, ForeignKey('ability.id'), primary_key=True)
    is_hidden: Mapped[bool] = mapped_column(Boolean)

    ability = relationship(Ability, foreign_keys=[ability_id],back_populates='pm_with_ability', lazy='joined')
    pm_summary = relationship(PmSummary, foreign_keys=[gen_id, form_id, nat_dex_nr], back_populates='abilities', lazy='joined')

    __table_args__ = (
        ForeignKeyConstraint(
            ['gen_id', 'form_id', 'nat_dex_nr'],
            ['pm_summary.gen_id', 'pm_summary.form_id', 'pm_summary.nat_dex_nr']),
        CheckConstraint(gen_id >= 3, name='Generation Check'),
    )

    def __init__(self, pm_summary: PmSummary, ability: Ability, is_hidden: bool = False):
        self.pm_summary = pm_summary
        self.gen_id = pm_summary.gen_id
        self.form_id = pm_summary.form_id
        self.nat_dex_nr = pm_summary.nat_dex_nr
        self.ability = ability
        self.ability_id = ability.id
        self.is_hidden = is_hidden

### Functions used in table setup

def add_relation_to_table(data: PmHasAbilityData):
    try:
        pm_has_ability = session.query(PmHasAbility).filter_by(
            gen_id=data.pm_summary.gen_id,
            form_id=data.pm_summary.form_id,
            nat_dex_nr=data.pm_summary.nat_dex_nr,
            ability_id=data.ability.id,
            is_hidden=data.hidden
        ).first()
        if pm_has_ability == None:
            pm_has_ability = PmHasAbility(
            pm_summary=data.pm_summary,
            ability=data.ability,
            is_hidden=data.hidden
        )
        session.add(pm_has_ability)
    except Exception as error:
        print(f"Error adding relation to table: {error}")
        session.rollback()

def test_relation_inserts():
    test_inserts = get_test_insert_dicts()
    data: list[PmHasAbilityData] = test_inserts
    try:
        for relation in data:
            add_relation_to_table(relation)
    except Exception as error:
        print(f"test data that was supposed to work failed: {error}")
    else:
        commit_and_close()
        print(f"test data inserted in pm_has_abilities")

def get_test_insert_dicts():
    levitate = get_ability_by_name("Levitate")
    sharpness = get_ability_by_name("Sharpness")
    steadfast = get_ability_by_name("Steadfast")
    justified = get_ability_by_name("Justified")
    pickup = get_ability_by_name("Pickup")
    thick_fat = get_ability_by_name("Thick Fat")
    gluttony = get_ability_by_name("Gluttony")
    clorophyll = get_ability_by_name("Clorophyll")
    leaf_guard = get_ability_by_name("Leaf Guard")
    infiltrator = get_ability_by_name("Infiltrator")
    rotom_gen4, rotom_wash_gen4, rotom_frost_gen4, rotom_fan_gen4, rotom_mow_gen4, rotom_heat_gen4 = get_summaries_by_gen(PmGen.GEN4)
    rotom_gen5, rotom_wash_gen5, rotom_frost_gen5, rotom_fan_gen5, rotom_mow_gen5, rotom_heat_gen5, gallade_gen5, skiploom_gen5, munchlax_gen5 = get_summaries_by_gen(PmGen.GEN5)
    gallade_gen9 = get_summaries_by_gen(PmGen.GEN9)[0]
    pm_summaries = [
        rotom_gen4, rotom_frost_gen4, rotom_wash_gen4, rotom_fan_gen4, rotom_mow_gen4, rotom_heat_gen4,
        rotom_gen5, rotom_frost_gen5, rotom_wash_gen5, rotom_fan_gen5, rotom_mow_gen5, rotom_heat_gen5,
        gallade_gen5, gallade_gen5,
        gallade_gen9, gallade_gen9, gallade_gen9,
        skiploom_gen5, skiploom_gen5, skiploom_gen5,
        munchlax_gen5, munchlax_gen5, munchlax_gen5
    ]
    abilities = [
        #Rotom
        levitate, levitate, levitate, levitate, levitate, levitate,
        levitate, levitate, levitate, levitate, levitate, levitate,
        #Gallade
        steadfast, justified,
        steadfast, sharpness, justified,
        #Skiploom
        clorophyll, leaf_guard, infiltrator,
        #Munchlax
        pickup, thick_fat, gluttony
    ]
    hidden = [
        #Rotom
        False, False, False, False, False, False,
        False, False, False, False, False, False,
        #Gallade
        False, True,
        False, False, True,
        #Skiploom
        False, False, True,
        #Munchlax
        False, False, True
    ]
    working_data = get_list_of_objects_by_template(
        PmHasAbilityData,
        pm_summaries,
        abilities,
        hidden
    )
    return working_data
