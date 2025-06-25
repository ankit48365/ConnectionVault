"""Test script for connection manager in ConnectionVault."""
# local poetry build
# running from connectionvault @ file:///home/ankiz/Documents/mygit/ConnectionVault/dist/connectionvault-0.0.4-py3-none-any.whl # pylint: disable=line-too-long
from app.src.connection_manager import main # pylint: disable=import-error

def test():
    """Test function to load connections, choose one, and execute a query."""
    main()
    # print(df)

if __name__ == "__main__":
    test()
