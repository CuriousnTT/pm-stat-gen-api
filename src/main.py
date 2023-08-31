#Dependencies
import uvicorn
from pmalchemy.alchemy import clean_database, make_database, show_all_tables
from pmgens.pmgen import getGenerationsTable
from pmtypes.pmtypes import getTypesTable, getTypeRelationshipTable

if __name__ == "__main__":

    #Set up SQL Database
    #show_all_tables()
    clean_database()
    make_database()

    #Fill Database
    getGenerationsTable()
    getTypesTable()
    getTypeRelationshipTable()

    #Set up API
    uvicorn.run("api:app", host="127.0.0.1", reload=True)

