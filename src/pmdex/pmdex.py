from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.pmalchemy.alchemy import Base, session, get_or_create, commit_and_close
from src.pmgens.generations import Generation
from src.pmtypes.pmtypes import PmType
from src.pmdex.evolutions import EvolutionStage, get_all_evolution_stages

class PmDex(Base):
    __tablename__='pmdex'

    nat_dex_nr: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)
    dex_header: Mapped[str] = mapped_column(String(45))
    evolution_stage_id: Mapped[int] = mapped_column(Integer, ForeignKey('evolution_stage.id'))
    
    evolution_stage: Mapped[EvolutionStage] = relationship('EvolutionStage', foreign_keys=[evolution_stage_id])

    def __init__(self, nat_dex_nr: int, name: str, dex_header: str, evolution_stage: EvolutionStage):
        self.nat_dex_nr = nat_dex_nr
        self.name = name
        self.dex_header = dex_header
        self.evolution_stage_id = evolution_stage.id
        self.evolution_stage = evolution_stage

    def __repr__(self):
        return self.name
    
### Functions used in table setup

def four_test_inserts():
    baby, base, middle, final = get_all_evolution_stages()
    ids = []
    inserts = []
    insert_one = {
        "nat_dex_nr": 479,
        "name": "Rotom",
        "dex_header": "Plasma Pokémon",
        "evolution_stage": base
        }
    inserts.append(insert_one)
    insert_two = {
        "nat_dex_nr": 475,
        "name": "Gallade",
        "dex_header": "Blade Pokémon",
        "evolution_stage": final
    }
    inserts.append(insert_two)
    insert_three = {
        "nat_dex_nr": 188,
        "name": "Skiploom",
        "dex_header": "Cottonweed Pokémon",
        "evolution_stage": middle
    }
    inserts.append(insert_three)
    insert_four = {
        "nat_dex_nr": 446,
        "name": "Munchlax",
        "dex_header": "Big Eater Pokémon",
        "evolution_stage": baby
    }
    inserts.append(insert_four)
    for insert in inserts:
        get_or_create(
            PmDex,
            nat_dex_nr=insert["nat_dex_nr"],
            name=insert["name"],
            dex_header=insert["dex_header"],
            evolution_stage=insert["evolution_stage"])
        ids.append(insert["nat_dex_nr"])
    commit_and_close()
    print(f"test data inserted in pmdex at nat_dex_nrs: {ids}")

### Functions using pmdex

def get_by_nat_dex_nr(nr: int):
    try:
        entry = session.get(PmDex, nr)
        return entry
    except Exception as error:
        print(f"An error occurred when contacting pmdex: {error}")