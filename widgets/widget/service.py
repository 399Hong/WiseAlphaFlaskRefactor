import utils
from flask import jsonify, request,current_app
import sqlite3


def create_widget() -> dict:
    conn = None
    widget = request.get_json()
    response = {}
    try:
        conn = utils.get_db_connection(current_app.config['DATABASE'])
        cur = conn.cursor()
        cur.execute("INSERT INTO widget (name) VALUES (?)", (widget.get('name'), ))
        cur.close()
        conn.commit()
        response['status'] = 201
    except sqlite3.Error as error :
        print("Error while working with SQLite.", error)
        conn.rollback()
        response['status'] = 500


    finally:
        if conn:
            conn.close()

    return response
def getWidgetbyName(name :str) -> list:

    conn = None
    widgets = []
    try:
        conn = utils.get_db_connection(current_app.config['DATABASE'])
        where_clause = ''
        # for filtering names

        if name: 
            where_clause = f"WHERE name like ?"
            seq = ("%"+name+"%",)

        else:
            seq = tuple()

        cur = conn.cursor()
        query = f"SELECT id, name FROM widget {where_clause} ORDER BY name"

        for row in cur.execute(query,seq):
            widgets.append({
                "id": row[0],
                "name": row[1],
            })
        cur.close()
    except sqlite3.Error as error :

        print("Error while working with SQLite.", error)
        widgets.append({"status":500})

    finally:
        if conn:
            conn.close()
    return widgets

# all the methods can be combined into one and refactor into a database repo
def getWidgetbyID(id:int) -> dict:
    conn = None
    response = {}
    try:
        conn = utils.get_db_connection(current_app.config['DATABASE'])
        cur = conn.cursor()
        query = "SELECT id, name FROM widget WHERE id = ?"
        widget_row = cur.execute(query, (id, )).fetchone()
        cur.close()
        if widget_row:
            response = {
                "id": widget_row[0],
                "name": widget_row[1],
            }
        else:
            response['status'] = 404

    except sqlite3.Error as error :
        print("Error while working with SQLite.", error)
        response['status'] = 500

    finally:
        if conn:
            conn.close()

    return response
def deleteWidgetbyID(id:int) -> dict:
    conn = None
    response = {}
    try:
        conn = utils.get_db_connection(current_app.config['DATABASE'])
        cur = conn.cursor()
        query = "DELETE FROM widget WHERE id = ?"
        cur.execute(query, (id, ))

        rowcount = cur.rowcount
        print(rowcount)
        cur.close()
        conn.commit()
        # postive rowcount means delete successful
        if rowcount > 0:
            response ['status'] = 204
        else:
            response ['status'] = 404


    except sqlite3.Error as error :
        print("Error while working with SQLite.", error)
        response['status'] = 500
        conn.rollback()

    finally:
        if conn:
            conn.close()

    return response
def updateWidgetbyID(id:int) -> dict:
    conn = None
    response = {}
    try:
        conn = utils.get_db_connection(current_app.config['DATABASE'])
        cur = conn.cursor()
        widget = request.get_json()
        cur.execute("UPDATE widget SET name = ? WHERE id = ?", (widget.get('name'), id, ))

        rowcount = cur.rowcount
        cur.close()
        conn.commit()
        # postive rowcount means update successful
        if rowcount > 0:
            response ['status'] = 204
        else:
            response ['status'] = 404

    except sqlite3.Error as error :
        print("Error while working with SQLite.", error)
        response['status'] = 500
        conn.rollback()

    finally:
        if conn:
            conn.close()

    return response


#
def createWidgetOption(id) -> dict:
    conn = None
    option = request.get_json()
    print(option)

    response = {}
    try:

        conn = utils.get_db_connection(current_app.config['DATABASE'])
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute("INSERT INTO widget_option (name, value, widget_id) VALUES (?, ?, ?)", (
            option.get('name'),
            option.get('value'),
            id,
        ))
        
        rowcount = cur.rowcount
        cur.close()
        conn.commit()
        # postive rowcount means update successful
        if rowcount > 0:
            response ['status'] = 201
        else:
            response ['status'] = 404
    except sqlite3.Error as error :
        print("Error while working with SQLite.", error)
        conn.rollback()
        response['status'] = 500


    finally:
        if conn:
            conn.close()

    return response
def getWidgetOptionByWidgetID(id) -> dict:
    conn = None
    response = {}
    try:
        conn = utils.get_db_connection(current_app.config['DATABASE'])
        cur = conn.cursor()
        query = "SELECT id, name, value, widget_id FROM widget_option WHERE widget_id = ? ORDER BY name"
        response = []
        for row in cur.execute(query, (id, )):
            response.append({
                "id": row[0],
                "name": row[1],
                "value": row[2],
                "widget_id": row[3],
            })

        cur.close()
  

    except sqlite3.Error as error :
        print("Error while working with SQLite.", error)
        conn.rollback()
        response['status'] = 500


    finally:
        if conn:
            conn.close()

    return response



def updateWidgetOptionByID(id) -> dict:

    conn = None
    option = request.get_json()

    response = {}
    try:

        conn = utils.get_db_connection(current_app.config['DATABASE'])
        cur = conn.cursor()
        query = "UPDATE widget_option SET name = ?, value = ? WHERE id = ?"
        cur.execute(query, (
            option.get('name'),
            option.get('value'),
            id
        ))
        
        rowcount = cur.rowcount
        cur.close()
        conn.commit()
        # postive rowcount means update successful
        if rowcount > 0:
            response ['status'] = 204
        else:
            response ['status'] = 404
    except sqlite3.Error as error :
        print("Error while working with SQLite.", error)
        conn.rollback()
        response['status'] = 500


    finally:
        if conn:
            conn.close()

    return response
def getWidgetOptionByID(id) -> dict:
    conn = None

    response = {}
    try:

        conn = utils.get_db_connection(current_app.config['DATABASE'])
        cur = conn.cursor()
        query =  "SELECT id, name, value, widget_id FROM widget_option WHERE id = ?"
        option_row = cur.execute(query, (id, )
        ).fetchone()

        if option_row:
            response = {
                "id": option_row[0],
                "name": option_row[1],
                "value": option_row[2],
                "widget_id": option_row[3],
            }
        else:
            response['status'] = 404
    except sqlite3.Error as error :
        print("Error while working with SQLite.", error)
        conn.rollback()
        response['status'] = 500


    finally:
        if conn:
            conn.close()

    return response
def deleteWidgetOptionByID(id:int) -> dict:
    conn = None
    response = {}
    try:
        conn = utils.get_db_connection(current_app.config['DATABASE'])
        cur = conn.cursor()
        query = "DELETE FROM widget_option WHERE id = ?"
        cur.execute(query, (id, ))

        rowcount = cur.rowcount
        print(rowcount)
        cur.close()
        conn.commit()
        # postive rowcount means delete successful
        if rowcount > 0:
            response ['status'] = 204
        else:
            response ['status'] = 404


    except sqlite3.Error as error :
        print("Error while working with SQLite.", error)
        response['status'] = 500
        conn.rollback()

    finally:
        if conn:
            conn.close()

    return response