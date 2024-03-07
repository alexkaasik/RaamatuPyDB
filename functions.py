from sqlite3 import *
from sqlite3 import Error

def create_connection(path:str):
    connection = None

    try:
        connection=connect(path)
        print("link")
    except Error as e:
        print(f"Error:{e}")

    return connection;

def Execute_Query(connection,query:str):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("tabel koik")
    except Error as e:
        print(f"tea:{e}")

def Execute_Query_Read(connection, query:str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result= cursor.fetchall()
        return result
    except Error as e:
        print(f"vaga:{e}")

def Execute_Query_Delete(connection, query:str):

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("\ndel tb/db\n")
    except Error as e:
        print(f"del:{e}")