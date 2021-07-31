class Product:

    def __init__(self, id, title, description, category, price, dateOfExpiry, inStock, freeDelivery):
        self._id = id
        self._title = title
        self._description = description
        self._category = category
        self._price = price
        self._dateOfExpriy = dateOfExpiry
        self._inStock = inStock
        self._freeDelivery = freeDelivery

    def getId(self):
        return self._id

    def getPrice(self):
        return self._price    

    def getDateOfExpiry(self):
        return self._dateOfExpriy
    
    def getInStock(self):
        return self._inStock

    def __eq__(self, o):
        return isinstance(o, Product) and o.__dict__ == self.__dict__
        
    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __repr__(self):
        return str(self.__dict__)