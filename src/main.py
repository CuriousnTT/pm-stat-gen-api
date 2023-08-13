#Dependencies
from typing import Union
from fastapi import FastAPI

#Locals
from pmstats.basestats import getBaseStats
from pmgens.genenum import PmGen

#Code
app = FastAPI()

@app.get("/")
def read_root():
    return {"info" : "Welcome to the world of pmStatGen-API! Go to /docs for information about how to use it!"}

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/stats/")
def get_stats_for_a_generation(q: Union[PmGen, None] = None):
    if q == None:
        return {"generation": "Defaults to 2 and later",
                "info": getBaseStats()}
    if q == PmGen:
        return {"generation": q, 
                "info": getBaseStats(q)}

@app.get("/generations")
def get_generations():
    return {"info": "These are the generations which currently exist and how you should refer to them when using this API",
            "generations": list(PmGen)}