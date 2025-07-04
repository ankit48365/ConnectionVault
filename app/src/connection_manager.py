"""Connection Manager for managing database connections using YAML file storage."""
import os
import yaml # pylint: disable=import-error
from tabulate import tabulate # pylint: disable=import-error

#readme.md file for setting up

# Retrieve and verify the environment variable
conn_home = os.getenv('conn_home')
# print(f"conn_home: {conn_home}")

# Define the path for the connections file
connections_file = os.path.join(conn_home, 'connections.yaml')
# print(f"connections_file: {connections_file}")

# Check if the file exists

if os.path.exists(connections_file):
    # print("File exists.")
    pass #pass is for doing nothing
else:
    print("File does not exist.")

# Function to load the connections from the file
def load_connections():
    """Load connections from the YAML file."""
    if os.path.exists(connections_file):
        with open(connections_file, 'r') as file:
            return yaml.safe_load(file) or {}
    return {}

# Function to save the connections to the file
def save_connections(connections):
    """Save connections to the YAML file."""
    with open(connections_file, 'w') as file:
        yaml.safe_dump(connections, file)

# Function to add or update a connection
def add_or_update_connection(name, details):
    """Add or update a connection in the YAML file."""
    connections = load_connections()
    connections[name] = details
    save_connections(connections)

# Function to delete a connection
def delete_connection(name):
    """Delete a connection from the YAML file."""
    connections = load_connections()
    if name in connections:
        del connections[name]
        save_connections(connections)

# Function to display connections and return the mapping of numbers to connection names
# def display_connections():
#     connections = load_connections()
#     if not connections:
#         print("No connections available.")
#         return []
#     connection_list = list(connections.items())
#     for i, (name, details) in enumerate(connection_list, 1):
#         print(f'{i}: {name} - {details}')
#     return connection_list


def display_connections():
    """Display connections in a tabular format."""
    connections = load_connections()
    if not connections:
        print("No connections available.")
        return []

    connection_list = [(name, details['ConnectionType'],details['driver'], details['database'], details['host'], details['port'], details['user']) # pylint: disable=line-too-long
                       for name, details in connections.items()]

    headers = ["Name", "Type", "driver", "Database", "Host", "Port", "User"]
    print(tabulate(connection_list, headers=headers, tablefmt="grid"))

    return connection_list



def main():
    """Main function to run the connection manager CLI."""
    while True:
        print("\nOptions: [0] Add New Connection [1] Update Connection [2] Delete Connection [3] Display Connections [4] Exit") # pylint: disable=line-too-long
        choice = input("Enter your choice: ")

        if choice == '0':
            # while True:
                # print("\Connection Type: [1] Postgres [2] SQL Server [3] other [4] Exit")
            ConnType = input("Connection Type: [1] Postgres [2] SQL Server [3] MySQL [4] Other [5] Exit ") # pylint: disable=line-too-long
            if ConnType == '1': ConnType = 'postgres'
            elif ConnType == '2': ConnType = 'sqlserver'
            elif ConnType == '3': ConnType = 'mysql'
            elif ConnType == '4': ConnType = 'other'
            elif ConnType == '5':
                break
            else:
                print("Invalid choice. Please try again.")

            name = input("Enter new connection name: ")
            driver = input("Enter driver name (suggestion ~ postgresql+psycopg2 or ODBC+Driver+18+for+SQL+Server or mysqlconnector): ") # pylint: disable=line-too-long
            host = input("Enter host: ")
            database = input("Enter database: ")
            port = input("Enter port: ")
            user = input("Enter user: ")
            password = input("Enter password: ")
            details = {'ConnectionType':ConnType,'driver':driver,'host': host,'database': database, 'port': port, 'user': user, 'password': password} # pylint: disable=line-too-long
            add_or_update_connection(name, details)
            print(f'Connection {name} added.')

        elif choice == '1':
            print("Select connection to update:")
            connection_list = display_connections()
            selection = int(input("Enter the connection number: "))
            if 1 <= selection <= len(connection_list):
                name = connection_list[selection - 1][0]
                connection_type = connection_list[selection - 1][1].get('ConnectionType', 'unknown')
                driver = input("Enter new driver (leave blank to keep current): ") or connection_list[selection - 1][1]['driver'] # pylint: disable=line-too-long
                host = input("Enter new host (leave blank to keep current): ") or connection_list[selection - 1][1]['host'] # pylint: disable=line-too-long
                database = input("Enter new database (leave blank to keep current): ") or connection_list[selection - 1][1]['database'] # pylint: disable=line-too-long
                port = input("Enter new port (leave blank to keep current): ") or connection_list[selection - 1][1]['port'] # pylint: disable=line-too-long
                user = input("Enter new user (leave blank to keep current): ") or connection_list[selection - 1][1]['user'] # pylint: disable=line-too-long
                password = input("Enter new password (leave blank to keep current): ") or connection_list[selection - 1][1]['password'] # pylint: disable=line-too-long
                details = {'ConnectionType':connection_type, 'driver':driver,'host': host, 'database': database,'port': port, 'user': user, 'password': password} # pylint: disable=line-too-long
                add_or_update_connection(name, details)
                print(f'Connection {name} updated.')
            else:
                print("Invalid selection.")

        elif choice == '2':
            print("Select connection to delete:")
            connection_list = display_connections()
            selection = int(input("Enter the connection number: "))
            if 1 <= selection <= len(connection_list):
                name = connection_list[selection - 1][0]
                delete_connection(name)
                print(f'Connection {name} deleted.')
            else:
                print("Invalid selection.")

        elif choice == '3':
            print("Current connections:")
            display_connections()

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

