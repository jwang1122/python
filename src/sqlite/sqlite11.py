"""
Create many-to-many relational tables
product-to-provider
"""

from sqlitehelper import *
from sqlite12 import *
class ProductDB:
    def __init__(self, db="mydb.db"):
        self.conn = create_connection(db)

    def createProductTable(self):
        try:
            sql = "CREATE TABLE product (id text, name text, series text, description text, price real)"
            create_table(self.__dict__conn, sql)
        except Exception as e:
            print(e)

    def createProviderTable(self):
        try:
            sql = "CREATE TABLE provider (id text, name text, address text, contact text)"
            create_table(self.conn, sql)
        except Exception as e:
            print(e)

    def createProdProviderTable(self):
        try:
            sql = "CREATE TABLE prod_prov(prodid text, providerid text)"
            create_table(self.conn, sql)
        except Exception as e:
            print(e)

    def insertProduct(self, product):
        try:
            c = self.conn.cursor()
            values = (product.id,product.name,product.series,product.model,product.price)
            c.execute('INSERT INTO product VALUES (?,?,?,?,?)', values)
            self.conn.commit()
        except Exception as error:
            print("Error:",error)

    def insertProvider(self,provider):
        try:
            c = conn.cursor()
            values = (provider.id,provider.name,provider.address,provider.contact)
            c.execute('INSERT INTO provider VALUES (?,?,?,?)', values)
            self.conn.commit()
        except Exception as error:
            print("Error:",error)

    def buildRelation(self, productid, providerid):
        try:
            c = self.conn.cursor()
            values = (productid, providerid)
            c.execute('INSERT INTO prod_prov VALUES (?,?)', values)
            self.conn.commit()
        except Exception as error:
            print("Error:",error)

    def findProvider(self, productid):
        try:
            providers = []
            c = self.conn.cursor()
            result = c.execute('select * from prod_prov where prodid=?',(productid,))
            for x in result:
                providers.append(self.getProviderById(x[1]))
            self.conn.commit()
            return providers
        except Exception as error:
            print("Error:",error)

    def getProviderById(self,providerid):
        try:
            c = self.conn.cursor()
            result = c.execute('select * from provider where id=?',(providerid,))
            prov = result.fetchone()
            provider = Provider(prov[1],prov[2],prov[3])
            provider.id = prov[0]
            self.conn.commit()
            return provider
        except Exception as error:
            print("Error:",error)

    def findProduct(self, providerid):
        try:
            products = []
            c = self.conn.cursor()
            result = c.execute('select * from prod_prov where providerid=?',(providerid,))
            for x in result:
                products.append(self.getProductById(x[0]))
            self.conn.commit()
            return products
        except Exception as error:
            print("Error:",error)

    def getProductById(self,productid):
        try:
            c = self.conn.cursor()
            result = c.execute('select * from product where id=?',(productid,))
            prod = result.fetchone()
            product = Product(prod[1],prod[2],prod[3], prod[4])
            product.id = prod[0]
            return product
            self.conn.commit()
        except Exception as error:
            print("Error:",error)

    def closeDB(self):
        self.conn.close()

if __name__ == '__main__':
    # conn = create_connection("mydb.db")
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

    # findProvider("86d5721ac10e41d3a02c93d62ef9ebe8", conn)
    # findProduct("45671d9ddf92419ebd4adf1bf0cd9a1a",conn)


    # conn.close()
    print("Done.")