from typing import Union
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pmgens.pmgen import PmGen, Generation
from pmalchemy.alchemy import Base, session, commit_and_close

class PmType(Base):
    __tablename__ = 'types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    generation_id: Mapped[int] = mapped_column(Integer, ForeignKey('generation.id'))
    generation: Mapped[Generation] = relationship('Generation', backref='types')
    
    def __init__(self, name: str, generation: Generation):
        self.name = name
        self.generation = generation
        self.generation_id = generation.id

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.name
    
class PmTypeRelations(Base):
    __tablename__ = 'type_relations'
    attack_type: Mapped[int] = mapped_column(Integer, ForeignKey('types.id'), primary_key=True)
    defending_type: Mapped[int] = mapped_column(Integer, ForeignKey('types.id'), primary_key=True)
    effectiveness: Mapped[float] = mapped_column(Float)

    def __init__(self, attack_type: int, defending_type: int, effectiveness: Union[float, None] = 1.0):
        self.attack_type = attack_type
        self.defending_type = defending_type
        self.effectiveness = effectiveness

#Default is generation 1
defaultTypes = {
    "normal": {
        "weak_to": ["fighting"], "resists": [None], "immune_to": ["ghost"]
    },
    "fire": {"weak_to": ["water", "ground", "rock"], "resists": ["fire", "grass", "bug"], "immune_to": [None]
    },
    "water": {
        "weakTo": ["electric", "grass"], "resists": ["fire", "water", "ice"], "immune_to": [None]
    },
    "electric": {
        "weak_to": ["ground"], "resists": ["electric", "flying"], "immune_to": [None]
    },
    "grass": {
        "weak_to": ["fire", "ice", "poison", "flying", "bug"], "resists": ["water", "electric", "grass", "ground"], "immune_to": [None]
    },
    "ice": {
        "weak_to": ["fire", "fighting", "rock"], "resists": ["ice"], "immune_to": [None]
    },
    "fighting": {
        "weak_to": ["flying", "psychic"], "resists": ["bug", "rock"], "immune_to": [None]
    },
    "poison": {
        "weak_to": ["ground", "psychic", "bug"], "resists": ["grass", "fighting", "poison"], "immune_to": [None]
    },
    "ground": {
        "weak_to": ["water", "grass", "ice"], "resists": ["poison", "rock"], "immune_to": ["electric"]
    },
    "flying": {
        "weak_to": ["electric", "ice", "rock"], "resists": ["grass", "fighting", "bug"], "immune_to": ["ground"]
    },
    "psychic": {
        "weak_to": ["bug"], "resists": ["fighting", "psychic"], "immune_to": ["ghost"] 
    },
    "bug": {
        "weak_to": ["fire", "flying", "rock"], "resists": ["grass", "fighting", "ground"], "immune_to": [None]
    },
    "rock": {
        "weak_to": ["water", "grass", "fighting", "ground"], "resists": ["normal", "fire", "poison", "flying"], "immune_to": [None]
    },
    "ghost": {
        "weak_to": ["ghost"], "resists": ["poison", "bug"], "immune_to": ["normal", "fighting"]
    },
    "dragon": {
        "weak_to": ["ice", "dragon"], "resists": ["fire", "water", "electric", "grass"], "immune_to": [None]
    }
}

gen2To5Changes = {
    "fire": {
        "weak_to": ["water", "ground", "rock"], "resists": ["fire", "grass", "bug", "steel"], "immune_to": [None]
    },
    "water": {
        "weak_to": ["electric", "grass"], "resists": ["fire", "water", "ice", "steel"], "immune_to": [None]
    },
    "electric": {
        "weak_to": ["ground"], "resists": ["electric", "flying", "steel"], "immune_to": [None]
    },
    "ice": {
        "weak_to": ["fire", "fighting", "rock", "steel"], "resists": ["ice"], "immune_to": [None]
    },
    "fighting": {
        "weak_to": ["flying", "psychic"], "resists": ["bug", "rock", "dark"], "immune_to": [None]
    },
    "poison": {
        "weak_to": ["ground", "psychic"], "resists": ["grass", "fighting", "poison", "bug"], "immune_to": [None]
    },
    "psychic": {
        "weak_to": ["bug", "ghost", "dark"], "resists": ["fighting", "psychic"], "immune_to": [None]
    },
    "bug": {
        "weak_to": ["fire", "flying", "rock"], "resists": ["grass", "fighting", "ground"], "immune_to": [None]
    },
    "rock": {
        "weak_to": ["water", "grass", "fighting", "ground", "steel"], "resists": ["normal", "fire", "poison", "flying"], "immune_to": [None]
    },
    "ghost": {
        "weak_to": ["ghost", "dark"], "resists": ["poison", "bug"], "immune_to": ["normal", "fighting"]
    },
    "dark": {
        "weak_to": ["fighting", "bug"], "resists": ["ghost", "dark"], "immune_to": ["psychic"]
    },
    "steel": {
        "weak_to": ["fire", "fighting", "ground"], "resists": ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel"], "immune_to": ["poison"]
    },
}

gen6ToCurrentChanges = {
    "fire": {
        "weak_to": ["water", "ground", "rock"], "resists": ["fire", "grass", "bug", "steel", "fairy"], "immune_to": [None]
    },
    "fighting": {
        "weak_to": ["flying", "psychic", "fairy"], "resists": ["bug", "rock", "dark"], "immune_to": [None]
    },
    "poison": {
        "weak_to": ["ground", "psychic"], "resists": ["grass", "fighting", "poison", "bug", "fairy"], "immune_to": [None]
    },
    "dragon": {
        "weak_to": ["ice", "dragon", "fairy"], "resists": ["fire", "water", "electric", "grass"], "immune_to": [None]
    },
    "dark": {
        "weak_to": ["fighting", "bug", "fairy"], "resists": ["ghost", "dark"], "immune_to": ["psychic"]
    },
    "steel": {
        "weak_to": ["fire", "fighting", "ground"], "resists": ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "dragon", "steel", "fairy"], "immune_to": ["poison"]
    },
    "fairy": {
        "weak_to": ["poison", "steel"], "resists": ["fighting", "bug", "dark"], "immune_to": ["dragon"]
    }
}

def getGenerationsForTypes():
    def q(x):
        return session.get(Generation, x)
    gen1 = q(1)
    gen2 = q(2)
    gen6 = q(6)
    return [gen1, gen2, gen6]

def addTypeToTable(name, gen:Generation):
        type = session.query(PmType).filter_by(
            name=name, generation=gen).first()
        if type is None:
            type = PmType(name=name, generation=gen)
            session.add(type)


def getTypesTable():
    [gen1, gen2, gen6] = getGenerationsForTypes()

    for name in defaultTypes:
        addTypeToTable(name, gen1)
    for name in gen2To5Changes:
        addTypeToTable(name, gen2)
    for name in gen6ToCurrentChanges:
        addTypeToTable(name, gen6)

    commit_and_close()

def getPmTypes(gen: PmGen):
    properties = defaultTypes.copy()

    if gen != PmGen.GEN1:
        properties.update(gen2To5Changes)
        if gen not in [PmGen.GEN2, PmGen.GEN3, PmGen.GEN4, PmGen.GEN5]:
            properties.update(gen6ToCurrentChanges)
    
    types = []

    for name in properties:
        types.append(name)

    return types

def getPmTypeById(id: int):
    pmtype = session.get(PmType, id)
    if pmtype is not None:
        info = {"type_name": pmtype.name,
                "type_id": pmtype.id,
                "last_changed": pmtype.generation.name,
                "generation_id": pmtype.generation_id}
        return info
    
def getPmTypesById(value: int):
    x = 0
    while x < value:
        x += 1
        getPmTypeById(x)

def getPmTypesByGeneration(gen: PmGen):
    generationTypes = {}
    if gen not in [PmGen.GEN1, PmGen.GEN2, PmGen.GEN3, PmGen.GEN4, PmGen.GEN5]:
        result = session.query(PmType).filter_by(generation_id = 6).all()
        for x in result:
            typedata = {
                "id": x.id,
                "name": x.name,
                "origin_generation": x.generation_id,
            }
            generationTypes[typedata["name"]] = typedata
            
    if gen is not PmGen.GEN1:
        result = session.query(PmType).filter_by(generation_id = 2).all()
        for x in result:
            typedata = {
                "id": x.id,
                "name": x.name,
                "origin_generation": x.generation_id,
            }
            if typedata["name"] not in generationTypes:
                generationTypes[typedata["name"]] = typedata
    
    result = session.query(PmType).filter_by(generation_id = 1).all()
    for x in result:
        typedata = {
            "id": x.id,
            "name": x.name,
            "origin_generation": x.generation_id,
        }   
        if typedata["name"] not in generationTypes:
                generationTypes[typedata["name"]] = typedata  

    return {"info": f"These are the types as they exist in {gen.value}. Their ids are essential for type relationships",
            "types": generationTypes,
            "generation": gen.value}