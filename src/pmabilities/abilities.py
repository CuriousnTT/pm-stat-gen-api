from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.pmalchemy.alchemy import Base, get_or_create, commit_and_close, session

class Ability(Base):
    __tablename__='ability'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

### Functions used in table setup

def some_test_abilities():
    report = []
    abilities = [
        {
            "name": "Levitate",
            "description": "This Pokemon is immune to Ground; Gravity/Ingrain/Smack Down/Iron Ball nullify it."
        },
        {
            "name": "Sharpness",
            "description": "This Pokemon's slicing moves have their power multiplied by 1.5."
        },
        {
            "name": "Steadfast",
            "description": "If this Pokemon flinches, its Speed is raised by 1 stage."
        },
        {   "name": "Justified",
            "description": "This Pokemon's Attack is raised by 1 stage after it is damaged by a Dark-type move."
        },
        {
            "name": "Pickup",
            "description": "If this Pokemon has no item, it finds one used by an adjacent Pokemon this turn."
        },
        {
            "name": "Thick Fat",
            "description": "Fire-/Ice-type moves against this Pokemon deal damage with a halved offensive stat."
        },
        {
            "name": "Gluttony",
            "description": "This Pokemon eats Berries at 1/2 max HP or less instead of the usual 1/4 max HP."
        },
        {
            "name": "Clorophyll",
            "description": "If Sunny Day is active, this Pokemon's Speed is doubled."
        },
        {
            "name": "Leaf Guard",
            "description": "If Sunny Day is active, this Pokemon cannot be statused and Rest will fail for it."
        },
        {
            "name": "Infiltrator",
            "description": "This Pokemon's moves ignore the foe's Reflect, Light Screen, Safeguard, and Mist."
        },
    ]
    try:
        for ability in abilities:
            name = ability["name"]
            description = ability["description"]
            ability = get_or_create(Ability, name=name, description=description)
            report.append(name)
    except Exception as error:
        print(f"Error adding ability to table: {error}")
        session.rollback()
    else:
        print(f"test abilities added to ability table: {report}")
    commit_and_close()

### Functions using table ability

def get_ability_by_name(name: str):
    try:
        ability = session.query(Ability).filter_by(name=name).first()
    except Exception as error:
        print(f"Error getting ability from table: {error}")
        session.rollback()
    else:
        return ability