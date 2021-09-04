"""
build many-to-many relationship
product-to-provider
"""
import uuid

class Product:
    def __init__(self, name, series=None, model=None, price=0.0):
        self.name = name
        self.id = uuid.uuid4().hex
        self.provider = []
        self.series = series
        self.model = model
        self.price = price

    def __repr__(self):
        return self.name
    
    def findProvider(self):
        pass

class Provider:
    def __init__(self, name, address=None, contact=None):
        self.id = uuid.uuid4().hex
        self.name = name
        self.contact = contact
        self.address = address
        self.product = []

    def __repr__(self):
        return self.name

    def loadProducts(self):
        pass

    