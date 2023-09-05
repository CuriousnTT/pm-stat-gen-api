from sqlalchemy import Integer, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pmalchemy.alchemy import Base, session, commit_and_close
from pmtypes.pmtypes import PmType, getGenerationsForTypes
from pmgens.pmgen import PmGen, getGenByShortName
from migrations.initialize import defaultTypes, gen2To5Changes, gen6ToCurrentChanges

class PmTypeRelations(Base):
    __tablename__ = 'type_relations'

    pm_type_chart_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('type_charts.id'), primary_key=True)
    attack_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('types.id'), primary_key=True)
    defending_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('types.id'), primary_key=True)
    effectiveness: Mapped[float] = mapped_column(Float)
    attack_type: Mapped[PmType] = relationship(
        'PmType', foreign_keys=[attack_type_id])
    defending_type: Mapped[PmType] = relationship(
        'PmType', foreign_keys=[defending_type_id])

    def __init__(self, attack_type: PmType, defending_type: PmType, type_chart_id: int, effectiveness: float):
        self.attack_type_id = attack_type.id
        self.attack_type = attack_type
        self.defending_type_id = defending_type.id
        self.defending_type = defending_type
        self.effectiveness = effectiveness
        self.pm_type_chart_id = type_chart_id

def addRelationToTable(attack_type: PmType, defending_type: PmType, type_chart_id: int, effectiveness: float):
    try:
        relation = session.query(PmTypeRelations).filter_by(
            pm_type_chart_id=type_chart_id,
            attack_type=attack_type,
            defending_type=defending_type).first()
        if relation is None:
            relation = PmTypeRelations(
                attack_type,
                defending_type,
                type_chart_id,
                effectiveness)
            session.add(relation)
    except Exception as e:
        print(f"Error adding relation to table: {e}")
        session.rollback()

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
    generation_ids = [1]

    for gen in getGenerationsForTypes():
        gen_id = gen.id
        types = session.query(PmType).filter(PmType.generation_id.in_(generation_ids)).all()
        chart_id = gen.type_chart_id

        for attack_type in types:
            attack_type_name = attack_type.name

            for defending_type in types:
                defending_type_name = defending_type.name
                defending_type_dict = getDefendingTypeDict(
                    gen_id, defending_type_name)
            
                effectiveness_value = calculate_effectiveness(attack_type_name, defending_type_dict)
            
                addRelationToTable(
                    attack_type,
                    defending_type,
                    chart_id,
                    effectiveness_value)
                
        if 2 not in generation_ids:
            generation_ids.append(2)
        else:
            generation_ids.append(6)
    
    commit_and_close()

def calculate_effectiveness(attack_type_name, defending_type_dict):
    effectiveness_value = 1.0
    if attack_type_name in defending_type_dict["weak_to"]:
        effectiveness_value = 2.0
    elif attack_type_name in defending_type_dict["resists"]:
        effectiveness_value = 0.5
    elif attack_type_name in defending_type_dict["immune_to"]:
        effectiveness_value = 0
    return effectiveness_value

def getPmTypeRelationMultiplier(gen: PmGen, attack_type_id: int, defending_type_id: int):
    try:
        generation = getGenByShortName(gen)
        relations = session.query(PmTypeRelations).filter_by(attack_type_id=attack_type_id, defending_type_id=defending_type_id).all()
        relations = [relation for relation in relations if relation.generation_id <= generation.id]
        return max(relations, key=lambda relation: relation.generation_id)
    except Exception as error:
        print(f"Error contacting type_relationship table: {error}")
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
        relations = session.query(PmTypeRelations).filter_by(defending_type_id=defending_type).all()
        relations = [relation for relation in relations if relation.pm_type_chart_id == generation.type_chart_id]      
        
        return relations
    except Exception as e:
        print(f"Error contacting type_relationship table: {e}")
        session.rollback()

def getOffensiveTypeRelations(gen: PmGen, attack_type: int):
    try:
        generation = getGenByShortName(gen)
        relations = session.query(PmTypeRelations).filter_by(attack_type_id=attack_type).all()
        relations = [relation for relation in relations if relation.pm_type_chart_id == generation.type_chart_id]

        return relations
    except Exception as e:
        print(f"Error contacting type_relationship table: {e}")
        session.rollback()