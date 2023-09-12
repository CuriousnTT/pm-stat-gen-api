#Dependencies
import uvicorn
from pmalchemy.alchemy import clean_database, make_database, show_all_tables
from pmgens.generations import get_generations_table
from pmgens.pmgames import get_game_table
from pmtypes.pmtypes import get_types_table
from pmtypes.typecharts import get_type_chart_table
from pmtypes.typerelations import get_type_relationship_table
from dataImport.stadiumConverter import PmStadiumConverter
pmsc = PmStadiumConverter("dataSets", "pm-stat-gen-api")

if __name__ == "__main__":

    #Set up SQL Database
    #show_all_tables()
    #TODO either remove clean_database after debugging or condition to run only in test environment
    clean_database()
    make_database()

    #Collecting pm data
    rentalStadium1PmsDict = pmsc.getStadiumData(1, "csv", True, True) #Change last parameter based on env
    rentalStadium1PmFull = pmsc.getStadiumData(1, "csv", False, True)
    
    #Fill Database
    get_type_chart_table()
    get_generations_table()
    get_game_table()
    get_types_table()
    get_type_relationship_table()

    #Set up API
    uvicorn.run("api:app", host="127.0.0.1", reload=True)
