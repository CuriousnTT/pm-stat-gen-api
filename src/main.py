#Dependencies
import uvicorn
import os
from pmalchemy.alchemy import clean_database, make_database, show_all_tables
from pmgens.generations import get_generations_table
from pmgens.pmgames import get_game_table
from pmtypes.pmtypes import get_types_table
from pmtypes.typecharts import get_type_chart_table
from pmtypes.typerelations import get_type_relationship_table

env = os.environ["ENV"]
host="127.0.0.1"
reload = True

def main():
    #Set up SQL Database
    #show_all_tables()
    if env != "prod":
        clean_database()
    make_database()
    
    #Fill Database
    get_type_chart_table()
    get_generations_table()
    get_game_table()
    get_types_table()
    get_type_relationship_table()

    #Set up API
    uvicorn.run("api:app", host=host, reload=reload)
