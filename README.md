[![Upload Python Package](https://github.com/ankit48365/ConnectionVault/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ankit48365/ConnectionVault/actions/workflows/python-publish.yml)
![Latest Release](https://img.shields.io/badge/release-v0.0.4-blue)

# ConnectionVault

## Purpose

The purpose of this project is to centralize the database connections file (as YAML) on a user's machine. The project has two utilities:

1. **Connection Manager:** Allows you to choose and load a connection string in a Python code quickly.

   Python code usage example:

   ```python
   from app.src.connection_utility import load_connections, choose_connection
   from sqlalchemy import create_engine
   import pandas as pd

   def main():
       connections = load_connections()
       conn = choose_connection(connections)

       engine = create_engine(conn)
       query = input("Input your query: ")
       df = pd.read_sql_query(query, engine)
       print(df)

   if __name__ == "__main__":
       main()

    
   
Linux:
echo 'export conn_home="path/outside/your/project/preferably"' >> ~/.bashrc
source ~/.bashrc

Windows: (takes a while for the new session to print the path)
setx conn_home "C:\path\outside\your\project\preferably"
echo %conn_home%

## Running the Project

To run this project, you need to define and save a path with the name `conn_home`. This is where you’ll save the `connections.yaml` file, which stores your database credentials.

### For Linux:

```bash
# Define and save the path in your .bashrc
echo 'export conn_home="path/outside/your/project/preferably"' >> ~/.bashrc

# Source the .bashrc to apply changes
source ~/.bashrc

## For Windows:

# Define and save the path
setx conn_home "C:\path\outside\your\project\preferably"

# Check the path
echo %conn_home%

# Define and save the path
setx conn_home "C:\path\outside\your\project\preferably"

# Check the path
echo %conn_home%
