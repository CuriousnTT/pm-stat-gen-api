from typing import Union
from dataclasses import dataclass
from sqlalchemy import Integer, Float, ForeignKey, UniqueConstraint, and_
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.pmalchemy.alchemy import Base, session, get_or_create, commit_and_close
from src.pmgens.generations import Generation, getGenByShortName
from src.pmgens.pmgen import PmGen
from src.pmtypes.pmtypes import PmType, getPmTypesById
from src.pmdex.pmforms import PmForm, get_form_by_name
from src.common.utils import get_list_of_objects_by_template

@dataclass
class PmSummaryData:
    generation: Generation
    form: PmForm
    primary_type: PmType
    secondary_type: Union[PmType, None]
    hit_points: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
    male_ratio: Union[float, None]

class PmSummary(Base):
    __tablename__ = 'pm_summary'

    gen_id: Mapped[int] = mapped_column(Integer, ForeignKey('generation.id'), primary_key=True)
    form_id: Mapped[int] = mapped_column(Integer, ForeignKey('form.id'), primary_key=True)
    nat_dex_nr: Mapped[int] = mapped_column(Integer, ForeignKey('form.nat_dex_nr'), primary_key=True)
    primary_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('types.id'))
    secondary_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('types.id'), nullable=True)
    hit_points: Mapped[int] = mapped_column(Integer)
    attack: Mapped[int] = mapped_column(Integer)
    defense: Mapped[int] = mapped_column(Integer)
    special_attack: Mapped[int] = mapped_column(Integer)
    special_defense: Mapped[int] = mapped_column(Integer)
    speed: Mapped[int] = mapped_column(Integer)
    male_ratio: Mapped[float] = mapped_column(Float, nullable=True)

    generation: Mapped[Generation] = relationship('Generation', foreign_keys=[gen_id])
    form: Mapped[PmForm] = relationship(
        'PmForm',
        foreign_keys=[form_id, nat_dex_nr],
        primaryjoin='and_(PmSummary.form_id == PmForm.id, PmSummary.nat_dex_nr == PmForm.nat_dex_nr)', backref='summaries')
    primary_type: Mapped[PmType] = relationship('PmType', foreign_keys=[primary_type_id], backref='primary_type_summaries')
    secondary_type: Mapped[PmType] = relationship('PmType', foreign_keys=[secondary_type_id], backref='secondary_type_summaries')

    def __init__(
        self,
        generation: Generation,
        form: PmForm,
        primary_type: PmType,
        secondary_type: Union[PmType, None],
        hit_points: int,
        attack: int,
        defense: int,
        special_attack: int,
        special_defense: int,
        speed: int,
        male_ratio: Union[float, None]
    ):
        if hit_points <= 0 or attack <= 0 or defense <= 0 or special_attack <= 0 or special_defense <= 0 or speed <= 0:
            raise ValueError('All stats must be greater than zero.')
        
        if male_ratio is not None:
            if male_ratio < 0:
                raise ValueError(
                    "Male ratio must be a positive float. Values above 1 get divided by 10 until they are between 0 and 1."
                    )
            while male_ratio > 1:
                male_ratio /= 10

        if secondary_type == primary_type:
            secondary_type = None
        if secondary_type is not None:
            self.secondary_type_id = secondary_type.id
        else:
            self.secondary_type_id = None

        self.generation = generation
        self.gen_id = generation.id
        self.form = form
        self.form_id = form.id
        self.nat_dex_nr = form.nat_dex_nr
        self.primary_type = primary_type
        self.primary_type_id = primary_type.id
        self.secondary_type = secondary_type
        self.hit_points = hit_points
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.male_ratio = male_ratio

### Functions used in table setup

def add_summary_to_table(data: PmSummaryData):
    try:
        get_or_create(
            PmSummary,
            generation=data.generation,
            form=data.form,
            primary_type=data.primary_type,
            secondary_type=data.secondary_type,
            hit_points=data.hit_points,
            attack=data.attack,
            defense=data.defense,
            special_attack=data.special_attack,
            special_defense=data.special_defense,
            speed=data.speed,
            male_ratio=data.male_ratio,
            )
    except Exception as error:
        print(f"Error adding summary to table: {error}")

def nine_test_forms():
    data: list[PmSummaryData] = get_test_insert_dicts()
    summary_list = []
    generation_list = []
    for summary in data:
        summary_list.append(summary.form.form_name)
        generation_list.append(summary.generation.id)
        add_summary_to_table(summary)
    commit_and_close()
    print(f"test data inserted in pm_summary for: {summary_list} in generations: {generation_list}")

def get_test_insert_dicts():
    type_ids = [1, 2, 3, 4, 5, 6, 7, 10, 11, 14]
    normal, fire, water, electric, grass, ice, fighting, flying, psychic, ghost = getPmTypesById(
        type_ids
    )
    gen2 = getGenByShortName(PmGen.GEN2)
    gen5 = getGenByShortName(PmGen.GEN5)
    gen4 = getGenByShortName(PmGen.GEN4)
    gen9 = getGenByShortName(PmGen.GEN9)
    rotom = get_form_by_name("Rotom")
    rotom_wash = get_form_by_name("Rotom-Wash")
    rotom_frost = get_form_by_name("Rotom-Frost")
    rotom_fan = get_form_by_name("Rotom-Fan")
    rotom_mow = get_form_by_name("Rotom-Mow")
    rotom_heat = get_form_by_name("Rotom-Heat")
    gallade = get_form_by_name("Gallade")
    skiploom = get_form_by_name("Skiploom")
    munchlax = get_form_by_name("Munchlax")
    generation_data = [
        #Rotom
        gen4, gen4, gen4, gen4, gen4, gen4,
        gen5, gen5, gen5, gen5, gen5, gen5,
        #Gallade
        gen5, gen9,
        #Skiploom
        gen5, gen2,
        #Munchlax
        gen5]
    form_data = [
        #Rotom gen4
        rotom, rotom_wash, rotom_frost, rotom_fan, rotom_mow, rotom_heat,
        #Rotom gen5
        rotom, rotom_wash, rotom_frost, rotom_fan, rotom_mow, rotom_heat,
        #Gallade
        gallade, gallade,
        #Skiploom
        skiploom, skiploom,
        munchlax]
    primary_type_data = [
        #Rotom gen4
        electric, electric, electric, electric, electric, electric,
        #Rotom gen5
        electric, electric, electric, electric, electric, electric,
        psychic, psychic,
        grass, grass,
        normal]
    secondary_type_data = [
        #Rotom
        ghost, ghost, ghost, ghost, ghost, ghost, ghost,
        water, ice, flying, grass, fire,
        #Gallade
        fighting, fighting,
        #Skiploom
        flying, flying,
        #Munchlax
        None]
    hit_point_stat_data = [
        #Rotom
        50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
        #Gallade
        68, 68,
        #Skiploom
        55, 55,
        #Munchlax
        135]
    attacK_stat_data = [
        #Rotom
        50, 65, 65, 65, 65, 65, 50, 65, 65, 65, 65, 65,
        #Gallade
        125, 125,
        #Skiploom
        45, 45,
        #Munchlax
        85]
    defense_stat_data = [
        #Rotom
        77, 107, 107, 107, 107, 107, 77, 107, 107, 107, 107, 107,
        #Gallade
        65, 65,
        #Skiploom
        50, 50,
        #Munchlax
        40]
    special_attack_stat_data = [
        #Rotom
        95, 105, 105, 105, 105, 105, 95, 105, 105, 105, 105, 105, 
        #Gallade
        65, 65,
        #Skiploom
        45, 45,
        #Munchlax
        40]
    special_defense_stat_data = [
        #Rotom
        77, 107, 107, 107, 107, 107, 77, 107, 107, 107, 107, 107,
        #Gallade
        115, 115,
        #Skiploom
        65, 65,
        #Munchlax
        85]
    speed_stat_data = [
        #Rotom
        91, 86, 86, 86, 86, 86, 91, 86, 86, 86, 86, 86,
        #Gallade
        80, 80,
        #Skiploom
        80, 80,
        #Munchlax
        5]
    male_ratio_gender_data = [
        #Rotom
        None, None, None, None, None, None, None, None, None, None, None, None,
        #Gallade
        1.0, 1.0,
        #Skiploom
        0.5, 0.5,
        #Munchlax
        0.875]
    return get_list_of_objects_by_template(
        PmSummaryData,
        generation_data,
        form_data,
        primary_type_data,
        secondary_type_data,
        hit_point_stat_data,
        attacK_stat_data,
        defense_stat_data,
        special_attack_stat_data,
        special_defense_stat_data,
        speed_stat_data,
        male_ratio_gender_data)

### Functions using pm_summary

def get_summaries_by_dex_nr(dex_nr: int):
    try:
        response = session.query(PmSummary).filter_by(nat_dex_nr=dex_nr).all()
    except Exception as error:
        print(f"Error getting summaries from table: {error}")
    else:
        return response

def get_summaries_by_gen_and_dex_nr(gen: PmGen, dex_nr: int):
    try:
        gen_id_subquery = session.query(
            Generation.id
        ).filter_by(
            name=gen.value
        ).scalar_subquery()
        summaries = session.query(
            PmSummary
        ).filter(
            and_(
                PmSummary.gen_id == gen_id_subquery,
                PmSummary.nat_dex_nr == dex_nr
            )
        ).all()
    except Exception as error:
        print(f"Error getting summaries from table: {error}")
    else:
        return summaries
    
def get_summaries_by_gen(gen: PmGen):
    try:
        gen_id_subquery = session.query(
            Generation.id
        ).filter_by(
            name=gen.value
        ).scalar_subquery()
        summaries = session.query(
            PmSummary
        ).filter(
            PmSummary.gen_id == gen_id_subquery,
        ).all()
    except Exception as error:
        print(f"Error getting summaries from table: {error}")
    else:
        return summaries