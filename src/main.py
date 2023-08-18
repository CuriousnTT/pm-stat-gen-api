#Dependencies
import subprocess, uvicorn
from sqlalchemy import text, MetaData, Table, Column, Integer, String

if __name__ == "__main__":

    #Set up SQL Database
    #DATABASE_PATH="pmdb/pmdb.sqlite3"
    #SOURCE="pmdb/pmdb.sql"
    ALCHEMY_PATH=".\src\pmalchemy\alchemy.py"
    run_sqlalchemy = f"python {ALCHEMY_PATH}"
    subprocess.call(run_sqlalchemy)
    #build_db_tables = f"sqlite3 {DATABASE_PATH} --init  {SOURCE}; .exit"
    #subprocess.call(build_db_tables)

    #Set up API
    uvicorn.run("api:app", host="127.0.0.1", reload=True)

