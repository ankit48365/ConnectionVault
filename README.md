[![Upload Python Package](https://github.com/ankit48365/ConnectionVault/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ankit48365/ConnectionVault/actions/workflows/python-publish.yml)
![Latest Release](https://img.shields.io/badge/release-v0.0.4-blue)

# ConnectionVault

To run this project :
define and save a path with name "conn_home", where you'll save connections.yaml file to save store your database credentials:

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

# Define and save the path
setx conn_home "C:\path\outside\your\project\preferably"

# Check the path
echo %conn_home%


<!-- # Navigate to your project directory -->
<!-- cd /path/to/your/project

# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
# venv\Scripts\activate  # For Windows

# Install Poetry inside the virtual environment
pip install poetry

# Initialize the Poetry project if not already done
poetry init
ead
