import sqlite3
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for s in {'A','B','C','D'}:
    print(s)
for char in "123":
    print(char)
for line in open("data/students.csv"):
    print(line, end='')

database = "pythonsqlite.db"
conn = create_connection(database)
c = conn.cursor()

for row in c.execute('select * from tasks'):
    print(row)

