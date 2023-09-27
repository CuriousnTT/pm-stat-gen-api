from typing import Union
from sqlalchemy import Integer, Float, ForeignKey, and_
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.pmalchemy.alchemy import Base, session, get_or_create, commit_and_close
from src.pmgens.generations import Generation, getGenByShortName
from src.pmgens.pmgen import PmGen
from src.pmtypes.pmtypes import PmType, getPmTypesById
from src.pmdex.pmforms import PmForm, get_form_by_name

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
            generation: generation,
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

def add_summary_to_table(dict):
    try:
        generation: Generation = dict["generation"]
        form: PmForm = dict["form"]
        primary_type: PmType = dict["primary_type"]
        secondary_type: Union[PmType, None] = dict["secondary_type"]
        hit_points = dict["hit_points"]
        attack = dict["attack"]
        defense = dict["defense"]
        special_attack = dict["special_attack"]
        special_defense = dict["special_defense"]
        speed = dict["speed"]
        male_ratio = dict["male_ratio"]
        get_or_create(
            PmSummary,
            generation=generation,
            form=form,
            primary_type=primary_type,
            secondary_type=secondary_type,
            hit_points=hit_points,
            attack=attack,
            defense=defense,
            special_attack=special_attack,
            special_defense=special_defense,
            speed=speed,
            male_ratio=male_ratio,
            )
        print(f"Added {form.form_name} to PmSummary in generation {generation.id}")
    except Exception as error:
        print(f"Error adding summary to table: {error}")

def nine_test_forms():
    dicts = get_test_insert_dicts()
    summary_list = []
    generation_list = []
    for form in dicts:
        summary_list.append(form["form"].form_name)
        generation_list.append(form["generation"].id)
        add_summary_to_table(form)
    commit_and_close()
    print(f"test data inserted in pmforms for: {summary_list} in generations: {generation_list}")

def get_test_insert_dicts():
    type_ids = [1, 2, 3, 4, 5, 6, 7, 10, 11, 14]
    normal, fire, water, electric, grass, ice, fighting, flying, psychic, ghost = getPmTypesById(
        type_ids
    )
    gen5 = getGenByShortName(PmGen.GEN5)
    gen4 = getGenByShortName(PmGen.GEN4)
    rotom = get_form_by_name("Rotom")
    rotom_wash = get_form_by_name("Rotom-Wash")
    rotom_frost = get_form_by_name("Rotom-Frost")
    rotom_fan = get_form_by_name("Rotom-Fan")
    rotom_mow = get_form_by_name("Rotom-Mow")
    rotom_heat = get_form_by_name("Rotom-Heat")
    gallade = get_form_by_name("Gallade")
    skiploom = get_form_by_name("Skiploom")
    munchlax = get_form_by_name("Munchlax")
    dicts = [
        {
        "generation": gen4,
        "form": rotom,
        "primary_type": electric,
        "secondary_type": ghost,
        "hit_points": 50,
        "attack": 50,
        "defense": 77,
        "special_attack": 95,
        "special_defense": 77,
        "speed": 91,
        "male_ratio": None,
        },
        {
        "generation": gen4,
        "form": rotom_wash,
        "primary_type": electric,
        "secondary_type": ghost,
        "hit_points": 50,
        "attack": 65,
        "defense": 107,
        "special_attack": 105,
        "special_defense": 107,
        "speed": 86,
        "male_ratio": None,
        },
        {
        "generation": gen4,
        "form": rotom_frost,
        "primary_type": electric,
        "secondary_type": ghost,
        "hit_points": 50,
        "attack": 65,
        "defense": 107,
        "special_attack": 105,
        "special_defense": 107,
        "speed": 86,
        "male_ratio": None,
        },
        {
        "generation": gen4,
        "form": rotom_fan,
        "primary_type": electric,
        "secondary_type": ghost,
        "hit_points": 50,
        "attack": 65,
        "defense": 107,
        "special_attack": 105,
        "special_defense": 107,
        "speed": 86,
        "male_ratio": None,
        },
        {
        "generation": gen4,
        "form": rotom_mow,
        "primary_type": electric,
        "secondary_type": ghost,
        "hit_points": 50,
        "attack": 65,
        "defense": 107,
        "special_attack": 105,
        "special_defense": 107,
        "speed": 86,
        "male_ratio": None,
        },
        {
        "generation": gen4,
        "form": rotom_heat,
        "primary_type": electric,
        "secondary_type": ghost,
        "hit_points": 50,
        "attack": 65,
        "defense": 107,
        "special_attack": 105,
        "special_defense": 107,
        "speed": 86,
        "male_ratio": None,
        },
        {
        "generation": gen5,
        "form": rotom,
        "primary_type": electric,
        "secondary_type": ghost,
        "hit_points": 50,
        "attack": 50,
        "defense": 77,
        "special_attack": 95,
        "special_defense": 77,
        "speed": 91,
        "male_ratio": None,
        },
        {
        "generation": gen5,
        "form": rotom_wash,
        "primary_type": electric,
        "secondary_type": water,
        "hit_points": 50,
        "attack": 65,
        "defense": 107,
        "special_attack": 105,
        "special_defense": 107,
        "speed": 86,
        "male_ratio": None,
        },
        {
        "generation": gen5,
        "form": rotom_frost,
        "primary_type": electric,
        "secondary_type": ice,
        "hit_points": 50,
        "attack": 65,
        "defense": 107,
        "special_attack": 105,
        "special_defense": 107,
        "speed": 86,
        "male_ratio": None,
        },
        {
        "generation": gen5,
        "form": rotom_fan,
        "primary_type": electric,
        "secondary_type": flying,
        "hit_points": 50,
        "attack": 65,
        "defense": 107,
        "special_attack": 105,
        "special_defense": 107,
        "speed": 86,
        "male_ratio": None,
        },
        {
        "generation": gen5,
        "form": rotom_mow,
        "primary_type": electric,
        "secondary_type": grass,
        "hit_points": 50,
        "attack": 65,
        "defense": 107,
        "special_attack": 105,
        "special_defense": 107,
        "speed": 86,
        "male_ratio": None,
        },
        {
        "generation": gen5,
        "form": rotom_heat,
        "primary_type": electric,
        "secondary_type": fire,
        "hit_points": 50,
        "attack": 65,
        "defense": 107,
        "special_attack": 105,
        "special_defense": 107,
        "speed": 86,
        "male_ratio": None,
        },
        {
        "generation": gen5,
        "form": gallade,
        "primary_type": psychic,
        "secondary_type": fighting,
        "hit_points": 68,
        "attack": 125,
        "defense": 65,
        "special_attack": 65,
        "special_defense": 115,
        "speed": 80,
        "male_ratio": 1.0,
        },
        {
        "generation": gen5,
        "form": skiploom,
        "primary_type": grass,
        "secondary_type": flying,
        "hit_points": 55,
        "attack": 45,
        "defense": 50,
        "special_attack": 45,
        "special_defense": 65,
        "speed": 80,
        "male_ratio": 0.5,
        },
        {
        "generation": gen5,
        "form": munchlax,
        "primary_type": normal,
        "secondary_type": None,
        "hit_points": 135,
        "attack": 85,
        "defense": 40,
        "special_attack": 40,
        "special_defense": 85,
        "speed": 5,
        "male_ratio": 0.875,
        },
    ]
    return dicts

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
        ).subquery()
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
