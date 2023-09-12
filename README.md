PM-Stat-Gen-API v.0.1
######
This is an API-service based on FastAPI and sqlite3 intended to provide data on pokemon at a given level, with:
1. a random nature, 
2. with no Effort Values (EVs), 
3. with random Individual Values (IVs),
4. with a gender valid for the pokemon at the correct frequency,
5. with the last 4 moves the pokemon should have learned at that level,
6. based on the correct generation,
7. and if relevant, game from the generation, 
8. with the possibility to override these values with values valid for the generation.

To set it up locally:
1. Ensure you have poetry installed by running the following in bash (add -k if it fails to verify) curl -sSL https://install.python-poetry.org | python3 -
2. Clone the repository
3. Run poetry shell. This will set up a virtual environment for the project.
4. Run poetry install. This will install the required dependencies from pyproject.toml
5. Execute the main.py file by running the following command: 
initialize
Specify environment for test or production by writing initialize -env test or initialize -env prod. If no argument is offered, it defaults to development mode.

This will set up the database using sqlite3, populate the database, and activate the API from the local port 127.0.0.1:8000.
Visit the port/docs for a list of supported api-calls and how to use them.