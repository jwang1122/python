"""
Create many-to-many relational tables
product-to-provider
"""

from sqlitehelper import *
from sqlite12 import *

def createProductTable(conn):
    try:
        sql = "CREATE TABLE product (id text, name text, series text, description text, price real)"
        create_table(conn, sql)
    except Exception as e:
        print(e)

def createProviderTable(conn):
    try:
        sql = "CREATE TABLE provider (id text, name text, address text, contact text)"
        create_table(conn, sql)
    except Exception as e:
        print(e)

def createProdProviderTable(conn):
    try:
        sql = "CREATE TABLE prod_prov(prodid text, providerid text)"
        create_table(conn, sql)
    except Exception as e:
        print(e)

def insertProduct(product, conn):
    try:
        c = conn.cursor()
        values = (product.id,product.name,product.series,product.model,product.price)
        c.execute('INSERT INTO product VALUES (?,?,?,?,?)', values)
        conn.commit()
    except Exception as error:
        print("Error:",error)

def insertProvider(provider, conn):
    try:
        c = conn.cursor()
        values = (provider.id,provider.name,provider.address,provider.contact)
        c.execute('INSERT INTO provider VALUES (?,?,?,?)', values)
        conn.commit()
    except Exception as error:
        print("Error:",error)

def buildRelation(productid, providerid, conn):
    try:
        c = conn.cursor()
        values = (productid, providerid)
        c.execute('INSERT INTO prod_prov VALUES (?,?)', values)
        conn.commit()
    except Exception as error:
        print("Error:",error)

def findProvider(productid, conn):
    try:
        c = conn.cursor()
        result = c.execute('select * from prod_prov where prodid=?',(productid,))
        for x in result:
            getProviderById(x[1], conn)
        conn.commit()
    except Exception as error:
        print("Error:",error)

def getProviderById(providerid, conn):
    try:
        c = conn.cursor()
        result = c.execute('select * from provider where id=?',(providerid,))
        prov = result.fetchone()
        provider = Provider(prov[1],prov[2],prov[3])
        provider.id = prov[0]
        print(provider)
        conn.commit()
    except Exception as error:
        print("Error:",error)

def findProduct(providerid, conn):
    try:
        c = conn.cursor()
        result = c.execute('select * from prod_prov where providerid=?',(providerid,))
        for x in result:
            getProductById(x[0], conn)
        conn.commit()
    except Exception as error:
        print("Error:",error)

def getProductById(productid, conn):
    try:
        c = conn.cursor()
        result = c.execute('select * from product where id=?',(productid,))
        prod = result.fetchone()
        product = Product(prod[1],prod[2],prod[3], prod[4])
        product.id = prod[0]
        print(product)
        conn.commit()
    except Exception as error:
        print("Error:",error)

if __name__ == '__main__':
    conn = create_connection("mydb.db")
    # createProductTable(conn)
    # createProviderTable(conn)
    # createProdProviderTable(conn)

    # product = Product("angle grinder", "AV1234","4-1/2 1375A",50.69)
    # insertProduct(product, conn)
    # product = Product("Jigsaw", "JT-122","5.0Amp 6 speed",26.99)
    # insertProduct(product, conn)
    # product = Product("Jigsaw Blades", "JT-233","T-Shank 14-Piece",19.98)
    # insertProduct(product, conn)
    # product = Product("Engraving Machine Kit", "2021 M2 CNC","3-Axis Up to 4x8ft",1198.00)
    # insertProduct(product, conn)

    # provider = Provider("Bosch", "123 Main Street, TX 77036", "John 713-234-4982")
    # insertProvider(provider, conn)

    # buildRelation("86d5721ac10e41d3a02c93d62ef9ebe8", "b0aa3de911804e61aa9ed5f265207729",conn)
    # buildRelation("1f842a20d4274fdab1e4449f482adf8b", "45671d9ddf92419ebd4adf1bf0cd9a1a",conn)
    # buildRelation("e87a2c93e84f45a48222889480a4c9f6", "45671d9ddf92419ebd4adf1bf0cd9a1a",conn)

    # provider = Provider("DEWALT", "789 Bellaire, TX 77479", "David 281-234-4982")
    # insertProvider(provider, conn)
    # buildRelation("86d5721ac10e41d3a02c93d62ef9ebe8", "dc16485b0e8945469bb53078edd18ef1",conn)

    # provider = Provider("YOVYOV", "321 University, TX 77479", "Allen 832-234-4982")
    # insertProvider(provider, conn)
    # buildRelation("86d5721ac10e41d3a02c93d62ef9ebe8", "45671d9ddf92419ebd4adf1bf0cd9a1a",conn)

    findProvider("86d5721ac10e41d3a02c93d62ef9ebe8", conn)
    findProduct("45671d9ddf92419ebd4adf1bf0cd9a1a",conn)


    conn.close()
    print("Done.")