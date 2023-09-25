#Dependencies
import uvicorn
import os
from src.pmalchemy.alchemy import clean_database, make_database, show_all_tables
from src.pmdex.evolutions import get_evolution_stage_table
from src.pmdex.pmdex import four_test_inserts
from src.pmdex.pmforms import four_test_pms
from src.pmgens.generations import get_generations_table
from src.pmgens.pmgames import get_game_table
from src.pmnatures.natures import get_nature_table
from src.pmtypes.pmtypes import get_types_table
from src.pmtypes.typecharts import get_type_chart_table
from src.pmtypes.typerelations import get_type_relationship_table

def main():
    env = os.environ["ENV"]
    host="127.0.0.1"
    reload = True
    #Set up SQL Database
    #show_all_tables()
    if env != "prod":
        clean_database()
    make_database()
    
    #Fill Database
    get_type_chart_table()
    get_evolution_stage_table()
    get_nature_table()
    get_generations_table()
    get_game_table()
    get_types_table()
    get_type_relationship_table()
    four_test_inserts()
    four_test_pms()

    #Set up API
    uvicorn.run("api:app", app_dir="src", host=host, reload=reload)
