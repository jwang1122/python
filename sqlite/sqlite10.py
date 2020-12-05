import sqlite3
from sqlite6 import *
import uuid

if __name__ == '__main__':
    database = "book.db"

    conn = create_connection(database)
    try:
        c = conn.cursor()
        books = [(uuid.uuid4().hex, 'Python - I', 10.88, 'John Wang', True),
                    (uuid.uuid4().hex, 'Python - II', 7.55, 'Elle Fu', False),
                    (uuid.uuid4().hex, 'Python - III', 12.00, 'Alex Liang', False),
                    ]
        c.executemany('INSERT INTO books VALUES (?,?,?,?,?)', books)
        conn.commit()
    except Exception as error:
        print("Error:",error)
    conn.close()
    
    print("Done.")