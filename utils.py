import os
import sqlite3
from pathlib import Path

def getPath(fileName:str) -> str:
    script_path = Path(__file__).parent.absolute()
    return os.path.join(script_path, fileName)

def get_db_connection(database:str) -> sqlite3.Connection:
    return sqlite3.connect(database)