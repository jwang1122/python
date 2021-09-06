"""
build many-to-many relationship
product-to-provider
"""
import uuid
from sqlite11 import *

class Product:
    def __init__(self, name, series=None, model=None, price=0.0):
        self.name = name
        self.id = uuid.uuid4().hex
        self.providers = []
        self.series = series
        self.model = model
        self.price = price

    def __repr__(self):
        return self.name
    
    def findProviderById(self, db):
       self.providers = db.findProvider(self.id)

    def showProviders(self):
        print(self.providers)

class Provider:
    def __init__(self, name, address=None, contact=None):
        self.id = uuid.uuid4().hex
        self.name = name
        self.contact = contact
        self.address = address
        self.products = []

    def __repr__(self):
        return self.name

    def loadProducts(self, db):
        self.products = db.findProduct(self.id)

    def showProducts(self):
        print(self.products)

if __name__ == '__main__':
   db = ProductDB()
   product = db.getProductById("86d5721ac10e41d3a02c93d62ef9ebe8")
   print(product)
   product.findProviderById(db)
   product.showProviders()

   provider = db.getProviderById("b0aa3de911804e61aa9ed5f265207729")
   print(provider)
   provider.loadProducts(db)
   provider.showProducts()
   
   db.closeDB()
   