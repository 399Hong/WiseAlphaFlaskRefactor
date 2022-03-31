import functools

import os
import sqlite3
from pathlib import Path
from flask import current_app

def getPath(fileName:str) -> str:

    script_path = Path(__file__).parent.absolute()
    return os.path.join(script_path, fileName)

def get_db_connection(database:str) -> sqlite3.Connection:

    return sqlite3.connect(database)

def dbHandler(func):
    
    @functools.wraps(func)
    def wrapperDBHandler(*args, **kwargs):

        conn = None
        response = {}

        try:
            conn = get_db_connection(current_app.config['DATABASE'])
            response =  func(conn = conn, *args, **kwargs)


        except sqlite3.Error as error :
            print("Error while working with SQLite.", error)
            response['status'] = 500
            conn.rollback()

        finally:
            if conn:
                conn.close()

        return response

    return wrapperDBHandler