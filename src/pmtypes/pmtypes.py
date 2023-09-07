from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pmgens.pmgen import PmGen, Generation
from pmalchemy.alchemy import Base, session, commit_and_close, get_all_from_table
from pmtypes.typecharts import get_type_chart_for_gen
from migrations.initialize import defaultTypes

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
    
def getGenerationsForTypes():
    try:
        generation_ids = [1,2,6]
        generations = session.query(Generation).filter(Generation.id.in_(generation_ids)).all()
        return generations
    except Exception as error:
        print(f"Error contacting generation table: {error}")

def addTypeToTable(name, gen:Generation):
    try:
        type = session.query(PmType).filter_by(
            name=name, generation=gen).first()
        if type is None:
            type = PmType(name=name, generation=gen)
            session.add(type)
    except Exception as e:
        print(f"Error adding type to table: {e}")
        session.rollback()

def getTypesTable():
    gen1, gen2, gen6 = getGenerationsForTypes()

    for name in gen1Keys:
        addTypeToTable(name, gen1)
    for name in gen2Keys:
        addTypeToTable(name, gen2)
    for name in gen6Keys:
        addTypeToTable(name, gen6)

    commit_and_close()

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
        info = {"type_name": pmtype.name,
                "type_id": pmtype.id,
                "generation_id": pmtype.generation.id}
        return info
    
def getPmTypesById(ids: list[int]):
    type_list = {}
    for id in ids:
        pmtype = getPmTypeById(id)
        type_data = {
            "id": pmtype["type_id"],
            "name": pmtype["type_name"],
            "origin_generation": pmtype["generation_id"],
        }
        type_list[type_data["id"]] = type_data
    print(type_list)

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
