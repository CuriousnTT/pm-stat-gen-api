from itertools import groupby
from typing import Union
from sqlalchemy import Integer, String, Float, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pmgens.pmgen import PmGen, Generation, getGenByShortName
from pmalchemy.alchemy import Base, session, commit_and_close

#Default is generation 1
defaultTypes = {
    "normal": {
        "weak_to": ["fighting"], 
        "resists": [None], 
        "immune_to": ["ghost"]
    },
    "fire": {
        "weak_to": ["water", "ground", "rock"], 
        "resists": ["fire", "grass", "bug"], 
        "immune_to": [None]
    },
    "water": {
        "weak_to": ["electric", "grass"], 
        "resists": ["fire", "water", "ice"], 
        "immune_to": [None]
    },
    "electric": {
        "weak_to": ["ground"], 
        "resists": ["electric", "flying"], 
        "immune_to": [None]
    },
    "grass": {
        "weak_to": ["fire", "ice", "poison", "flying", "bug"], 
        "resists": ["water", "electric", "grass", "ground"], 
        "immune_to": [None]
    },
    "ice": {
        "weak_to": ["fire", "fighting", "rock"], 
        "resists": ["ice"], 
        "immune_to": [None]
    },
    "fighting": {
        "weak_to": ["flying", "psychic"], 
        "resists": ["bug", "rock"], 
        "immune_to": [None]
    },
    "poison": {
        "weak_to": ["ground", "psychic", "bug"], 
        "resists": ["grass", "fighting", "poison"], 
        "immune_to": [None]
    },
    "ground": {
        "weak_to": ["water", "grass", "ice"], 
        "resists": ["poison", "rock"], 
        "immune_to": ["electric"]
    },
    "flying": {
        "weak_to": ["electric", "ice", "rock"], 
        "resists": ["grass", "fighting", "bug"], 
        "immune_to": ["ground"]
    },
    "psychic": {
        "weak_to": ["bug"], 
        "resists": ["fighting", "psychic"], 
        "immune_to": ["ghost"] 
    },
    "bug": {
        "weak_to": ["fire", "flying", "rock"], 
        "resists": ["grass", "fighting", "ground"], 
        "immune_to": [None]
    },
    "rock": {
        "weak_to": ["water", "grass", "fighting", "ground"], 
        "resists": ["normal", "fire", "poison", "flying"], 
        "immune_to": [None]
    },
    "ghost": {
        "weak_to": ["ghost"], 
        "resists": ["poison", "bug"], 
        "immune_to": ["normal", "fighting"]
    },
    "dragon": {
        "weak_to": ["ice", "dragon"], 
        "resists": ["fire", "water", "electric", "grass"], 
        "immune_to": [None]
    }
}

gen2To5Changes = {
    "fire": {
        "weak_to": ["water", "ground", "rock"], 
        "resists": ["fire", "grass", "bug", "steel"], 
        "immune_to": [None]
    },
    "water": {
        "weak_to": ["electric", "grass"], 
        "resists": ["fire", "water", "ice", "steel"], 
        "immune_to": [None]
    },
    "electric": {
        "weak_to": ["ground"], 
        "resists": ["electric", "flying", "steel"], 
        "immune_to": [None]
    },
    "ice": {
        "weak_to": ["fire", "fighting", "rock", "steel"], 
        "resists": ["ice"], 
        "immune_to": [None]
    },
    "fighting": {
        "weak_to": ["flying", "psychic"], 
        "resists": ["bug", "rock", "dark"], 
        "immune_to": [None]
    },
    "poison": {
        "weak_to": ["ground", "psychic"], 
        "resists": ["grass", "fighting", "poison", "bug"], 
        "immune_to": [None]
    },
    "psychic": {
        "weak_to": ["bug", "ghost", "dark"], 
        "resists": ["fighting", "psychic"], 
        "immune_to": [None]
    },
    "bug": {
        "weak_to": ["fire", "flying", "rock"], 
        "resists": ["grass", "fighting", "ground"], 
        "immune_to": [None]
    },
    "rock": {
        "weak_to": ["water", "grass", "fighting", "ground", "steel"], 
        "resists": ["normal", "fire", "poison", "flying"], 
        "immune_to": [None]
    },
    "ghost": {
        "weak_to": ["ghost", "dark"], 
        "resists": ["poison", "bug"], 
        "immune_to": ["normal", "fighting"]
    },
    "dark": {
        "weak_to": ["fighting", "bug"],
        "resists": ["ghost", "dark"], 
        "immune_to": ["psychic"]
    },
    "steel": {
        "weak_to": ["fire", "fighting", "ground"], 
        "resists": ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel"], 
        "immune_to": ["poison"]
    },
}

gen6ToCurrentChanges = {
    "fire": {
        "weak_to": ["water", "ground", "rock"], 
        "resists": ["fire", "grass", "bug", "steel", "fairy"], 
        "immune_to": [None]
    },
    "fighting": {
        "weak_to": ["flying", "psychic", "fairy"], 
        "resists": ["bug", "rock", "dark"], 
        "immune_to": [None]
    },
    "poison": {
        "weak_to": ["ground", "psychic"], 
        "resists": ["grass", "fighting", "poison", "bug", "fairy"], 
        "immune_to": [None]
    },
    "dragon": {
        "weak_to": ["ice", "dragon", "fairy"], 
        "resists": ["fire", "water", "electric", "grass"], 
        "immune_to": [None]
    },
    "dark": {
        "weak_to": ["fighting", "bug", "fairy"], 
        "resists": ["ghost", "dark"], 
        "immune_to": ["psychic"]
    },
    "steel": {
        "weak_to": ["fire", "fighting", "ground"], 
        "resists": ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "dragon", "steel", "fairy"], 
        "immune_to": ["poison"]
    },
    "fairy": {
        "weak_to": ["poison", "steel"], 
        "resists": ["fighting", "bug", "dark"], 
        "immune_to": ["dragon"]
    }
}

gen1Keys = [key for key in defaultTypes]
gen2Keys = ["dark", "steel"]
gen6Keys = ["fairy"]

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

    generation_id: Mapped[int] = mapped_column(Integer, ForeignKey('generation.id'), primary_key=True)
    attack_type: Mapped[int] = mapped_column(Integer, ForeignKey('types.id'), primary_key=True)
    defending_type: Mapped[int] = mapped_column(Integer, ForeignKey('types.id'), primary_key=True)
    effectiveness: Mapped[float] = mapped_column(Float)
    generation: Mapped[Generation] = relationship('Generation', backref='type_relations')

    def __init__(self, attack_type: int, defending_type: int, generation: Generation, effectiveness: float = 1.0,):
        self.attack_type = attack_type
        self.defending_type = defending_type
        self.effectiveness = effectiveness
        self.generation = generation
        self.generation_id = generation.id


def getGenerationsForTypes():
    def q(x):
        return session.get(Generation, x)
    gen1 = q(1)
    gen2 = q(2)
    gen6 = q(6)
    return [gen1, gen2, gen6]

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

def addRelationToTable(attack_type: int, defending_type: int, generation: Generation, effectiveness: float):
    try:
        relation = session.query(PmTypeRelations).filter_by(generation=generation, attack_type=attack_type, defending_type=defending_type).first()
        if relation is None:
            relation = PmTypeRelations(attack_type, defending_type, generation, effectiveness)
            session.add(relation)
    except Exception as e:
        print(f"Error adding relation to table: {e}")
        session.rollback()


def getTypesTable():
    [gen1, gen2, gen6] = getGenerationsForTypes()

    for name in gen1Keys:
        addTypeToTable(name, gen1)
    for name in gen2Keys:
        addTypeToTable(name, gen2)
    for name in gen6Keys:
        addTypeToTable(name, gen6)

    commit_and_close()

def getDefendingTypeDict(gen_id: int, defending_type_name: str):
    if gen_id == 1:
        defending_type_dict = defaultTypes[defending_type_name]
    elif gen_id == 2:
        defending_type_dict = gen2To5Changes.get(
            defending_type_name, defaultTypes.get(
                defending_type_name, {}))
    elif gen_id == 6:
        defending_type_dict = gen6ToCurrentChanges.get(
            defending_type_name, gen2To5Changes.get(
                defending_type_name, defaultTypes.get(defending_type_name, {})))
    return defending_type_dict

def getTypeRelationshipTable():
    [gen1, gen2, gen6] = getGenerationsForTypes()
    generation_ids = [1]

    for gen in [gen1, gen2, gen6]:
        types = session.query(PmType).filter(PmType.generation_id.in_(generation_ids)).all()
        gen_id = gen.id

        for attack_type in types:
            attack_type_id = attack_type.id
            attack_type_name = attack_type.name

            for defending_type in types:
                defending_type_id = defending_type.id
                defending_type_name = defending_type.name
                defending_type_dict = getDefendingTypeDict(gen_id, defending_type_name)
            
                effectiveness_value = 1.0
                if attack_type_name in defending_type_dict["weak_to"]:
                    effectiveness_value = 2.0
                elif attack_type_name in defending_type_dict["resists"]:
                    effectiveness_value = 0.5
                elif attack_type_name in defending_type_dict["immune_to"]:
                    effectiveness_value = 0
            
                addRelationToTable(attack_type_id, defending_type_id, gen, effectiveness_value)
                
        if 2 not in generation_ids:
            generation_ids.append(2)
        else:
            generation_ids.append(6)
    
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
                "generation_id": pmtype.generation_id}
        return info
    
def getPmTypesById(ids: list[int]):
    typelist = {}
    for x in ids:
        pmtype = getPmTypeById(x)
        typedata = {
            "id": pmtype["type_id"],
            "name": pmtype["type_name"],
            "origin_generation": pmtype["generation_id"],
        }
        typelist[typedata["id"]] = typedata
    print(typelist)

def getPmTypesByGeneration(gen: PmGen):
    generationTypes = {}
    allIds = []
    result = session.query(PmType).filter_by(generation_id = 1).all()

    for type in result:
        typedata = {
            "id": type.id,
            "name": type.name,
            "origin_generation": type.generation_id,
        }   
        if typedata["name"] not in generationTypes:
                generationTypes[typedata["name"]] = typedata
                allIds.append(type.id)  

    if gen is not PmGen.GEN1:
        result = session.query(PmType).filter_by(generation_id = 2).all()
        for type in result:
            typedata = {
                "id": type.id,
                "name": type.name,
                "origin_generation": type.generation_id,
            }
            if typedata["name"] not in generationTypes:
                generationTypes[typedata["name"]] = typedata
                allIds.append(type.id)

    if gen not in [PmGen.GEN1, PmGen.GEN2, PmGen.GEN3, PmGen.GEN4, PmGen.GEN5]:
        result = session.query(PmType).filter_by(generation_id = 6).all()
        for type in result:
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
            "all_ids": allIds}

def getPmTypeRelationMultiplier(gen: PmGen, attack_type_id: int, defending_type_id: int):
    try:
        generation = getGenByShortName(gen)
        relations = session.query(PmTypeRelations).filter_by(attack_type=attack_type_id, defending_type=defending_type_id).all()
        relations = [relation for relation in relations if relation.generation_id <= generation.id]
        return max(relations, key=lambda relation: relation.generation_id)
    except Exception as e:
        print(f"Error contacting type_relationship table: {e}")
        session.rollback()
    
def getAllPmTypeRelations():
    try:
        relations = session.query(PmTypeRelations).all()
        return relations
    except Exception as e:
        print(f"Error contacting type_relations table: {e}")
        session.rollback()

def getDefensiveTypeRelations(gen: PmGen, defending_type: int):
    try:
        generation = getGenByShortName(gen)
        relations = session.query(PmTypeRelations).filter_by(defending_type=defending_type).all()
        relations = [relation for relation in relations if relation.generation_id <= generation.id]
        result = {}
        for relation in relations:
            if relation.attack_type not in result or relation.generation_id > result[relation.attack_type].generation_id:
                result[relation.attack_type] = relation
        
        return list(result.values())
    except Exception as e:
        print(f"Error contacting type_relationship table: {e}")
        session.rollback()

def getOffensiveTypeRelations(gen: PmGen, attack_type: int):
    try:
        generation = getGenByShortName(gen)
        relations = session.query(PmTypeRelations).filter_by(attack_type=attack_type).all()
        relations = [relation for relation in relations if relation.generation_id <= generation.id]
        result = {}
        for relation in relations:
            if relation.defending_type not in result or relation.generation_id > result[relation.defending_type].generation_id:
                result[relation.defending_type] = relation
        
        return list(result.values())
    except Exception as e:
        print(f"Error contacting type_relationship table: {e}")
        session.rollback()