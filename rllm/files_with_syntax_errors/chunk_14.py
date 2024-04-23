import sqlite3
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

def get_all_data(cursor):
    cursor.execute("SELECT * FROM data")
    return cursor.fetchall()

def get_all_data_by_id(cursor, id):
    cursor.execute("SELECT * FROM data WHERE id =?", (id,))
    return cursor.fetchone()

def get_all_data_by_name(cursor, name):
    cursor.execute("SELECT * FROM data WHERE name =?", (name,))
    return cursor.fetchone()

def get_all_data_by_name_and_id(cursor, name, id):
    cursor.execute("SELECT * FROM data WHERE name =? AND id =?", (name, id))
    return cursor.fetchone()

def get_all_data_by_name_and_id_and_type(cursor, name, id, type):
    cursor.execute("SELECT * FROM data WHERE name =? AND id =? AND type =?", (name, id, type))
    return cursor.fetchone()

def get_all_