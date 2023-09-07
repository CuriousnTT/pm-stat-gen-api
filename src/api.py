#Dependencies
from typing import Union, Literal
from fastapi import FastAPI

#Locals
from pmgens.pmgen import PmGen
from pmgens.pmgen import SupportedGen, getGenerations
from pmgens.pmgames import getGames
from pmstats.basestats import getBaseStats
from pmtypes.pmtypes import getPmTypeById, getPmTypesByGeneration, get_all_PmTypes
from pmtypes.typerelations import getAllPmTypeRelations, getPmTypeRelationMultiplier, getDefensiveTypeRelations, getOffensiveTypeRelations
from pmnatures.natures import getNature, getSpecificNatures, NatureRelevantStat

app = FastAPI()

@app.get("/")
def read_root():
    return {"info" : "Welcome to the world of pmStatGen-API! Go to /docs for information about how to use it!"}

@app.get("/items/{item_id}")
#Example to be removed/replaced when items are implemented
def get_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/stats")
def get_stats_for_a_generation(gen: Union[PmGen, None] = None):
    if gen == None:
        return {"generation": "Defaults to 2 and later",
                "data": getBaseStats()}
    else:
        return {"generation": gen, 
                "data": getBaseStats(gen)}

@app.get("/generations")
def get_generations():
    return {"info": "These are the generations which currently exist. To reference them with this API use the short_name",
            "generations": getGenerations()}

@app.get("/generations/supported")
def get_supported_generations():
    return {"info": "These are the generations currently supported by this API",
            "generations": list(SupportedGen)}

@app.get("/games")
def get_games():
    return getGames()

@app.get("/games/{generation}")
def get_games_from_one_generation(generation: PmGen):
    return getGames(generation)

@app.get("/types/all")
def get_all_types():
    return get_all_PmTypes()

@app.get("/type/{id}")
def get_type_by_id(id: int):
    return getPmTypeById(id)

@app.get("/type/{generation}/defending_type_id={defending_type_id}")
def get_defensive_type_properties(generation: PmGen, defending_type_id: int):
    return getDefensiveTypeRelations(generation, defending_type_id)

@app.get("/type/{generation}/attacking_type_id={attack_type_id}")
def get_offensive_type_properties(generation: PmGen, attack_type_id: int):
    return getOffensiveTypeRelations(generation, attack_type_id)

@app.get("/types/{generation}")
def get_types(generation: PmGen):
    return getPmTypesByGeneration(generation)

@app.get("/types/{generation}/{attack_type_id}/{defending_type_id}")
def get_type_effectiveness_multiplier(generation: PmGen, attack_type_id: int, defending_type_id: int):
    return getPmTypeRelationMultiplier(generation, attack_type_id, defending_type_id)

@app.get("/types/relations/all")
def get_all_type_relations():
    return getAllPmTypeRelations()

@app.get("/nature")
def get_a_random_nature():
    return getNature()

@app.get("/natures/{effect}/{stat}")
def get_natures_with_effect_on_stat(effect: Literal["boosts", "reduces"], stat: NatureRelevantStat):
    boosts: bool
    if effect == "boosts":
        boosts = True
    elif effect == "reduces":
        boosts = False
    return getSpecificNatures(stat, boosts)
