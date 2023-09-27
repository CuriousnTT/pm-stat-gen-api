from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.pmgens.pmgen import PmGen
from src.pmgens.generations import Generation
from src.pmalchemy.alchemy import Base, session, commit_and_close, get_all_from_table, get_or_create
from src.pmtypes.typecharts import get_type_chart_for_gen
from src.migrations.initialize import defaultTypes

gen1Keys = list(defaultTypes)
gen2Keys = ["dark", "steel"]
gen6Keys = ["fairy"]

class PmType(Base):
    __tablename__ = 'types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    generation_id: Mapped[int] = mapped_column(Integer, ForeignKey('generation.id'))
    
    generation: Mapped[Generation] = relationship(
        'Generation', foreign_keys=[generation_id], backref='types')
    
    def __init__(self, name: str, generation: Generation):
        self.name = name
        self.generation = generation

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.name
    
### Functions used in table setup

def getGenerationsForTypes():
    try:
        generation_ids = [1,2,6]
        generations = session.query(Generation).filter(Generation.id.in_(generation_ids)).all()
        return generations
    except Exception as error:
        print(f"Error contacting generation table: {error}")

def get_types_table():
    gen1, gen2, gen6 = getGenerationsForTypes()

    for name in gen1Keys:
        get_or_create(PmType, name=name, generation=gen1)
    for name in gen2Keys:
        get_or_create(PmType, name=name, generation=gen2)
    for name in gen6Keys:
        get_or_create(PmType, name=name, generation=gen6)

    commit_and_close()
    print("Type table ready")

### Functions using types

def getTypeRelevantPmGen(gen: PmGen):
    value: PmGen = gen
    if gen is not PmGen.GEN1:
        value = PmGen.GEN2
        if gen not in [PmGen.GEN2, PmGen.GEN3, PmGen.GEN4, PmGen.GEN5]:
            value = PmGen.GEN6
    return value

def getPmTypeById(id: int):
    pmtype = session.get(PmType, id)
    if pmtype is not None:
        return pmtype
    
def getPmTypesById(ids: list[int]):
    type_list = []
    for id in ids:
        pmtype = getPmTypeById(id)
        type_list.append(pmtype)
    return type_list

def get_pmtype_by_name(name: str):
    try:
        pmtype = session.query(PmType).filter_by(name=name).first()
    except Exception as error:
        print(f"Error getting type from table: {error}")
    else:
        return pmtype

def getPmTypesByGeneration(gen: PmGen):
    generationIds = [1]
    if gen is not PmGen.GEN1:
        generationIds.append(2)
        if gen not in [PmGen.GEN2, PmGen.GEN3, PmGen.GEN4, PmGen.GEN5]:
            generationIds.append(6)
    
    generationTypes = {}
    allIds = []
    types = get_all_from_table(PmType)
    types = [type for type in types if type.generation_id in generationIds]
    for type in types:
        typedata = {
            "id": type.id,
            "name": type.name,
            "origin_generation": type.generation_id,
        }   
        generationTypes[typedata["name"]] = typedata
        allIds.append(type.id)  

    return {"info": f"These are the types as they exist in {gen.value}. Their ids are essential for type relationships",
            "types": generationTypes,
            "generation": gen.value,
            "type_chart": get_type_chart_for_gen(gen),
            "all_ids": allIds}
            
def get_all_PmTypes():
    result = get_all_from_table(PmType)
    return result
