#Dependencies
from typing import Union
from fastapi import FastAPI

#Locals
from pmstats.basestats import getBaseStats

#Code
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/stats")
def read_item(q: Union[str, None] = None):
    
    if q == "gen1":
        return {"Generation": "1", 
                "Info": getBaseStats(q)}
    if q != "gen1":
        return {"Generation": "2 and later",
                "Info": getBaseStats(q)}
