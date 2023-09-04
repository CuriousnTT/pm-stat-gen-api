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
    print("Database successfully set up")

    #Fill Database
    getGenerationsTable()
    print("Generation table ready")
    getTypesTable()
    print("Type table ready")
    getTypeRelationshipTable()
    print("Type relationships table ready")

    #Set up API
    uvicorn.run("api:app", host="127.0.0.1", reload=True)

