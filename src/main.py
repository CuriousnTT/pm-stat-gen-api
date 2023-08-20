#Dependencies
import uvicorn
from pmalchemy.alchemy import clear_database, make_database, show_all_tables

if __name__ == "__main__":

    #Set up SQL Database
    #show_all_tables()
    #clear_database()
    #make_database()

    #Set up API
    uvicorn.run("api:app", host="127.0.0.1", reload=True)

