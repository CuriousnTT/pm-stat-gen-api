#Dependencies
import uvicorn
from pmalchemy.alchemy import clean_database, make_database, show_all_tables
from pmgens.generations import get_generations_table
from pmgens.pmgames import get_game_table
from pmdex.evolutions import get_evolution_stage_table
from pmdex.pmdex import four_test_inserts
from pmdex.pmforms import four_test_pms
from pmtypes.pmtypes import get_types_table
from pmtypes.typecharts import get_type_chart_table
from pmtypes.typerelations import get_type_relationship_table

if __name__ == "__main__":

    #Set up SQL Database
    #show_all_tables()
    clean_database()
    make_database()
    

    #Fill Database
    get_type_chart_table()
    get_evolution_stage_table()
    get_generations_table()
    four_test_inserts()
    four_test_pms()
    get_game_table()
    get_types_table()
    get_type_relationship_table()

    #Set up API
    uvicorn.run("api:app", host="127.0.0.1", reload=True)
