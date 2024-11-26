# local poetry build
# running from connectionvault @ file:///home/ankiz/Documents/mygit/ConnectionVault/dist/connectionvault-0.0.4-py3-none-any.whl

from app.src.connection_manager import main

from sqlalchemy import create_engine
import pandas as pd

def test():
    main()
    # print(df)

if __name__ == "__main__":
    test()