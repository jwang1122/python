import sqlite3
from sqlite3 import Error
from pprint import pprint
import uuid


class BookDB:
    def __init__(self, dbname, url=None):
        self.dbname = dbname
        self.url = url

    def getBookDB(self):
        self.conn = BookDB.create_connection(self.dbname)
        c = self.conn.cursor()
        return c

    # Retrieve All
    def getBooks(self):
        bookdb = self.getBookDB()
        bookList = []
        try:
            for row in bookdb.execute('select * from books'):
                book = self.getBookFromList(row)
                bookList.append(book)
        except Exception as e:
            print(e)

        return bookList

    # Create One
    def create(self, book):
        """
        Create a book in database
        """
        db = self.getBookDB()
        book['_id'] = uuid.uuid4().hex
        value = self.getValueFromBook(book)
        db.execute('INSERT INTO books VALUES (?,?,?,?,?)', value)
        self.conn.commit()
        return book.get('_id')

    def getBookFromList(self, row):
        book = {
            "_id": row[0],
            "title": row[1],
            "price": row[2],
            "author": row[3],
            "read": row[4],
        }
        return book

    def getValueFromBook(self, book):
        value = []
        value.append(book['_id'])
        value.append(book['title'])
        value.append(book['price'])
        value.append(book['author'])
        value.append(book['read'])
        return value

    @classmethod
    def create_connection(cls, db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        return conn

    @classmethod
    def create_table(cls, conn, create_table_sql):
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


if __name__ == '__main__':
    bookdb = BookDB("book.db")
    # test retrieve many
    books = bookdb.getBooks()
    pprint(books)

    # test create
    book = {
        "title": "Introduction of Java",
        "price": 12.69,
        "author": "John Wang",
        "read": False,
    }
    bookdb.create(book)


    print("Done.")