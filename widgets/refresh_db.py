import pathlib
import os
import sqlite3


def refresh_db(db_path=None):
    script_path = pathlib.Path(__file__).parent.absolute()
    sql_path = os.path.join(script_path, "widgets.sql")
    
    if not db_path:
        db_path = os.path.join(script_path, "widgets.db")
        if os.path.exists(db_path):
            os.remove(db_path)

    with open(sql_path) as f:
        sql = f.read()

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.executescript(sql)
    c.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    refresh_db()
