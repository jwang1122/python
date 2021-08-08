"""
Create many-to-many relational tables
"""

from sqlitehelper import *

def createProductTable():
    try:
        conn = create_connection("mydb.db")
        sql = "CREATE TABLE product (id text, name text, series text, description text, price real)"
        create_table(conn, sql)
    except Exception as e:
        print(e)

def createProviderTable():
    try:
        conn = create_connection("mydb.db")
        sql = "CREATE TABLE provider (id text, name text, address text, contact text)"
        create_table(conn, sql)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    createProductTable()
    createProviderTable()
    print("Done.")