import sqlite3
from sqlite3 import Error
"""
Create table with primary key
"""

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main(database):
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS item (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        detail_id int,
                                        FOREIGN KEY (detail_id) REFERENCES item_detail (id)
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS item_detail (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    price real,
                                    quantity integer,
                                    date_in text NOT NULL,
                                    stroage_location text NOT NULL
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    database = "data/pythonsqlite.db"
    main(database)

    print("Done.")