#Dependencies
from typing import Union, Literal
from fastapi import FastAPI

#Locals
from pmgens.genenum import PmGen
from pmgens.genenum import SupportedGen
from pmgens.pmgames import getGames
from pmstats.basestats import getBaseStats
from pmtypes.pmtypes import createPmTypes
from pmnatures.natures import getNature
from pmnatures.natures import getSpecificNatures
from pmnatures.natures import NatureRelevantStat

app = FastAPI()

@app.get("/")
def read_root():
    return {"info" : "Welcome to the world of pmStatGen-API! Go to /docs for information about how to use it!"}

@app.get("/items/{item_id}")
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

#Works
@app.get("/generations")
def get_generations():
    return {"info": "These are the generations which currently exist and how you should refer to them when using this API.",
            "generations": list(PmGen)}

#Works
@app.get("/generations/supported")
def get_supported_generations():
    return {"info": "These are the generations currently supported by this API",
            "generations": list(SupportedGen)}

#Works
@app.get("/games")
def get_games():
    return getGames()

#Does not work
@app.get("/games/{generation}")
def get_games_from_one_generation(generation: PmGen):
    return getGames(generation)

#Does not work
@app.get("/types/{generation}")
def get_types(generation: PmGen, asIntended: Union[bool, None] = None):
    if asIntended != None:
        return createPmTypes(generation, asIntended)
    return createPmTypes(generation)

#Works
@app.get("/nature")
def get_nature():
    return getNature()

#Works
@app.get("/natures/{effect}/{stat}")
def get_natures_with_effect_on_stat(effect: Literal["boosts", "reduces"], stat: NatureRelevantStat):
    boosts = True
    if effect == "reduces":
        boosts == False
    return getSpecificNatures(stat, boosts)
