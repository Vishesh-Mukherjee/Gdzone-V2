from abc import ABC, abstractmethod

class ProductInventory(ABC):

    @abstractmethod
    def addProduct(self, product):
        pass

    @abstractmethod
    def addProducts(self, *products):
        pass

    @abstractmethod
    def getProduct(self, productId):
        pass

    @abstractmethod
    def getProducts(self, *productIds):
        pass

    @abstractmethod
    def getProductListAdmin(self):
        pass

    @abstractmethod
    def getProductListCustomer(self):
        pass

    @abstractmethod
    def removeProduct(self, productId):
        pass

    @abstractmethod
    def removeProducts(self, *productIds):
        pass

    @abstractmethod
    def updateProduct(self, product):
        pass

    @abstractmethod
    def updateProducts(self, *products):
        pass