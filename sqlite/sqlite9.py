import sqlite3
from sqlite6 import *

if __name__ == '__main__':
    database = "book.db"
    
    sql_create_books_table = """ CREATE TABLE IF NOT EXISTS books (
                                        _id text PRIMARY KEY,
                                        title text NOT NULL,
                                        price real,
                                        author text,
                                        read boolean
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_books_table)
    else:
        print("Error! cannot create the database connection.")

    print("Done.")