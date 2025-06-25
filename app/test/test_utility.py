"""Test utility script to load connections and execute a query"""
# local poetry build
# running from connectionvault @ file:///home/ankiz/Documents/mygit/ConnectionVault/dist/connectionvault-0.0.4-py3-none-any.whl # pylint: disable=line-too-long

from src.connection_utility import (load_connections, choose_connection)  # pylint: disable=import-error
from sqlalchemy import create_engine # pylint: disable=import-error
import pandas as pd # pylint: disable=import-error

def main():
    """Main function to load connections, choose one, and execute a query."""
    connections = load_connections()
    conn = choose_connection(connections)
    print(conn)
    engine = create_engine(conn)

    # Check the connection string and run the appropriate query
    if 'psycopg2' in conn:
        query = "SELECT schema_name FROM information_schema.schemata;"
    elif 'ODBC' in conn:
        query = "SELECT name FROM sys.schemas;"
    else:
        query = input("Input your query: ")

    df = pd.read_sql_query(query, engine)
    print('If its not a custom query then by deault the test will print all the schema present in the choosen connection/database\n') # pylint: disable=line-too-long
    print(df)


if __name__ == "__main__":
    main()
