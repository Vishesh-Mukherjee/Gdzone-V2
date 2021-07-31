from abc import ABC, abstractmethod

class Cart:
    
    @abstractmethod
    def getAllCartItems(self, userId):
        pass

    @abstractmethod
    def getCartTotal(self, userId):
        pass

    @abstractmethod
    def addCartItem(self, userId, productId):
        pass

    @abstractmethod
    def removeCartItem(self, userId, productId):
        pass
