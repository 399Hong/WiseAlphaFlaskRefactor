
import utils
from flask import request,current_app
import sqlite3
from typing import Union
from contextlib import closing

@utils.dbHandler
def create_widget(conn : sqlite3.Connection) -> Union[list,dict]:

    widget = request.get_json()
    response = {}
    with closing(conn.cursor()) as cur:
        cur.execute("INSERT INTO widget (name) VALUES (?)", (widget.get('name'), ))
    
    conn.commit()
    response['status'] = 201
    return response
@utils.dbHandler
def getWidgetbyName(conn : sqlite3.Connection, name :str) ->  Union[list,dict]:

    response = []
 
    where_clause = ''
    # for filtering names

    if name: 
        where_clause = f"WHERE name like ?"
        seq = ("%"+name+"%",)

    else:
        seq = tuple()

    with closing(conn.cursor()) as cur:

        query = f"SELECT id, name FROM widget {where_clause} ORDER BY name"

        for row in cur.execute(query,seq):
            response.append({
                "id": row[0],
                "name": row[1],
            })

    return response


@utils.dbHandler
def getWidgetbyID(conn : sqlite3.Connection,id:int) -> Union[list,dict]:

    response = {}
    widget_row = None

    with closing(conn.cursor()) as cur:
        query = "SELECT id, name FROM widget WHERE id = ?"
        widget_row = cur.execute(query, (id, )).fetchone()

    if widget_row:
        response = {
            "id": widget_row[0],
            "name": widget_row[1],
        }
    else:
        response['status'] = 404


    return response

@utils.dbHandler
def deleteWidgetbyID(conn : sqlite3.Connection,id:int) -> Union[list,dict]:

    response = {}
    rowcount = 0

    with closing(conn.cursor()) as cur:
        query = "DELETE FROM widget WHERE id = ?"
        cur.execute(query, (id, ))

        rowcount = cur.rowcount
        cur.close()
    conn.commit()
    # postive rowcount means delete successful
    if rowcount > 0:
        response ['status'] = 204
    else:
        response ['status'] = 404

    return response

@utils.dbHandler
def updateWidgetbyID(conn : sqlite3.Connection,id:int) -> Union[list,dict]:

    response = {}
    rowcount = 0

    widget = request.get_json()
    with closing(conn.cursor()) as cur:

        cur.execute("UPDATE widget SET name = ? WHERE id = ?", (widget.get('name'), id, ))
        rowcount = cur.rowcount

    conn.commit()
    # postive rowcount means update successful
    if rowcount > 0:
        response ['status'] = 204
    else:
        response ['status'] = 404


    return response

""""""""
@utils.dbHandler
def createWidgetOption(conn : sqlite3.Connection,id:int) -> Union[list,dict]:

    option = request.get_json()
    response = {}
    rowcount = 0

    with closing(conn.cursor()) as cur:
        
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute("INSERT INTO widget_option (name, value, widget_id) VALUES (?, ?, ?)", (
            option.get('name'),
            option.get('value'),
            id,
        ))
        
        rowcount = cur.rowcount

    conn.commit()
    # postive rowcount means update successful
    if rowcount > 0:
        response ['status'] = 201
    else:
        response ['status'] = 404

    return response

@utils.dbHandler
def getWidgetOptionByWidgetID(conn : sqlite3.Connection,id:int) -> Union[tuple,dict]:

    response = {}

    with closing(conn.cursor()) as cur:
    
        query = "SELECT id, name, value, widget_id FROM widget_option WHERE widget_id = ? ORDER BY name"
        response = []
        for row in cur.execute(query, (id, )):
            response.append({
                "id": row[0],
                "name": row[1],
                "value": row[2],
                "widget_id": row[3],
            })


    return response


@utils.dbHandler
def updateWidgetOptionByID(conn : sqlite3.Connection,id:int) -> Union[list,dict]:


    option = request.get_json()
    response = {}
    rowcount = 0

    
    with closing(conn.cursor()) as cur:
    
        query = "UPDATE widget_option SET name = ?, value = ? WHERE id = ?"
        cur.execute(query, (
            option.get('name'),
            option.get('value'),
            id
        ))
        
        rowcount = cur.rowcount

    conn.commit()
    # postive rowcount means update successful
    if rowcount > 0:
        response ['status'] = 204
    else:
        response ['status'] = 404


    return response

@utils.dbHandler
def getWidgetOptionByID(conn : sqlite3.Connection,id:int) -> Union[list,dict]:

    response = {}
    option_row = None

    with closing(conn.cursor()) as cur:
        conn = utils.get_db_connection(current_app.config['DATABASE'])
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

    return response

@utils.dbHandler
def deleteWidgetOptionByID(conn : sqlite3.Connection,id:int) -> Union[list,dict]:

    response = {}
    rowcount = None

    with closing(conn.cursor()) as cur:
    
        query = "DELETE FROM widget_option WHERE id = ?"
        cur.execute(query, (id, ))
        rowcount = cur.rowcount
  
    conn.commit()
    # postive rowcount means delete successful
    if rowcount > 0:
        response ['status'] = 204
    else:
        response ['status'] = 404

    return response