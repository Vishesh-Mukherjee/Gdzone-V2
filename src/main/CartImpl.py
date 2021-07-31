from Cart import Cart
from ProductInventoryImpl import ProductInventoryImpl
from Product import Product

class CartImpl(Cart):

    _userCart = {}

    def getAllCartItems(self, userId):
        if userId in self._userCart.keys():
            return self._userCart[userId]
        else:
            raise Exception("User Not Found")

    def getCartTotal(self, userId):
        total = 0.0
        if userId in self._userCart.keys():
            for each_product in self._userCart[userId]:
                total += each_product.getPrice()
            return total
        else:
            raise Exception("User Not Found")

    def addCartItem(self, userId, productId):
        productInventory = ProductInventoryImpl()
        if userId in self._userCart.keys():
            self._userCart[userId].append(productInventory.getProduct(productId))
        else:
            self._userCart.update({userId : [productInventory.getProduct(productId)]})

    def removeCartItem(self, userId, productId):
        if userId in self._userCart.keys():
            for each_product in self._userCart[userId]:
                if each_product.getId() == productId:
                    self._userCart[userId].remove(each_product)
        else: 
            raise Exception("User Not Found")