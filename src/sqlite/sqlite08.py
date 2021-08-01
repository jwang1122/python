"""
Retrieve relational data from projects and tasks tables
"""
import sqlite3
from sqlite2 import create_connection

if __name__ == '__main__':
    database = "pythonsqlite.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        t = (3,) # find all tasks related to this project.
        for row in c.execute('select * from projects where id=?',t):
            print(row)

        for row in c.execute('select * from tasks where project_id=?',t):
            print(row) # pull tasks from project

        t = (33309,) # find project related to this task.
        for row in c.execute('select project_id from tasks where id=?',t):
            print("21:",row) # pull project from a task
            for project in c.execute('select * from projects where id=?',row):
                print("23:",project)

    except Exception as error:
        print("Error:", error)
    conn.close()
    print("Done.")
