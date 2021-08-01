import sqlite3
from sqlite2 import create_connection
"""
Create relational data table by using primary key and foriener key fields
"""

if __name__ == '__main__':
    database = "pythonsqlite.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        projects = [
            (1, 'project-1', '2020-03-28', '2020-04-28'),
            (2, 'project-2', '2020-05-01', '2020-08-31'),
            (3, 'project-3', '2020-07-06', '2020-07-30'),
        ]
        c.executemany('INSERT INTO projects VALUES (?,?,?,?)', projects)
        conn.commit()
        tasks = [
            (11, 'task-11', 10, 1, '2020-03-28', '2020-04-28'),
            (12, 'task-12', 5, 1, '2020-04-01', '2020-04-10'),
            (13, 'task-13', 5, 1, '2020-04-10', '2020-04-15'),
        ]
        c.executemany('INSERT INTO tasks VALUES (?,?,?,?,?,?)', tasks)
        # the following is very important statement, otherwise no data will be stored into database
        conn.commit()
        tasks = [
            (21, 'task-21', 5, 2, '2020-05-28', '2020-05-28'),
            (22, 'task-22', 9, 2, '2020-05-01', '2020-05-10'),
            (23, 'task-23', 9, 2, '2020-05-10', '2020-08-15'),
        ]
        c.executemany('INSERT INTO tasks VALUES (?,?,?,?,?,?)', tasks)
        # the following is very important statement, otherwise no data will be stored into database
        conn.commit()
        tasks = [
            (31, 'task-31', 5, 3, '2020-04-10', '2020-04-12'),
            (32, 'task-32', 9, 3, '2020-04-13', '2020-04-14'),
            (33, 'task-33', 9, 3, '2020-05-15', '2020-04-15'),
        ]
        c.executemany('INSERT INTO tasks VALUES (?,?,?,?,?,?)', tasks)
        # the following is very important statement, otherwise no data will be stored into database
        conn.commit()
    except Exception as error:
        print("Error:", error)
    conn.close()
    print("Done.")
