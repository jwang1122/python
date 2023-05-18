import sqlite3
from sqlite3 import Error
from pprint import pprint
import uuid
from datetime import datetime

class BlackJackDB:
    def __init__(self, dbname, url=None):
        self.dbname = dbname


    # Create One
    def create(self, blackjack):
        """
        Create a blackjack in database
        """
        db = self.getBlackJackDB()
        value = self.getValueFromBlackjack(blackjack)
        db.execute('INSERT INTO blackjack VALUES (?,?,?,?,?)', value)
        self.conn.commit()
        return self.getBlackjack(value[0])

    # Retrieve All
    def getBlackjacks(self):
        db = self.getBlackJackDB()
        blackjackList = []
        try:
            for row in db.execute('select * from blackjack'):
                blackjack = self.getBlackjackFromList(row)
                blackjackList.append(blackjack)
        except Exception as e:
            print("line-32:", e)

        return blackjackList

    # Retrieve one
    def getBlackjack(self, id):
        """
        Retrieve a expense from database by id
        """
        db = self.getBlackJackDB()
        expense=None
        try:
            value = (id,)
            db.execute('select * from blackjack where id=?',value)
            blackjack = self.getBlackjackFromList(db.fetchone())
        except Exception as e:
            print(e)
        return blackjack

    def getBlackJackDB(self):
        self.conn = BlackJackDB.create_connection(self.dbname)
        c = self.conn.cursor()
        return c

    def getBlackjackFromList(self, row):
        blackjack = {
            "id": row[0],
            "name": row[1],
            "win": row[2],
            "loss": row[3],
            "tie": row[3],
        }
        return blackjack

    def getValueFromBlackjack(self, blackjack):
        value = []
        value.append(uuid.uuid4().hex)
        value.append(blackjack['name'])
        value.append(blackjack['win'])
        value.append(blackjack['loss'])
        value.append(blackjack['tie'])
        return value

    @classmethod
    def create_connection(cls, db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            # print(sqlite3.version)
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
    # conn = BlackJackDB.create_connection("data/blackjack.db")
    # sql = """
    #     CREATE TABLE IF NOT EXISTS blackjack (
    #         id text PRIMARY KEY,
    #         name text NOT NULL,
    #         win integer,
    #         loss integer,
    #         tie integer
    #     )
    # """
    # BlackJackDB.create_table(conn, sql)

    db = BlackJackDB("data/blackjack.db")

    blackjack = {
        "id":uuid.uuid4().hex,
        'name':'John',
        'win':1,
        "loss":0,
        "tie":0,
    }
    # db.create(blackjack)

    blackjack = {
        "id":uuid.uuid4().hex,
        'name':'dealer',
        'win':0,
        "loss":1,
        "tie":0,
    }
    # db.create(blackjack)

    all = db.getBlackjacks()
    pprint(all)