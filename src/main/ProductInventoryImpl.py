from Product import Product
from ProductInventory import ProductInventory
from datetime import datetime

from DateUtil import DateUtil

class ProductInventoryImpl(ProductInventory):

    _productList = []

    def __init__(self):
        if len(self._productList) == 0:
            p1 = Product(101, "Iphone", "Iphone 11 Max Pro", "Electronics", 99999.99, None, True, True)
            p2 = Product(102, "Sandwich", "Cheese Sandwich", "Food & Beverage", 299.99, DateUtil.stringToDate("31-10-2021"), True, True)
            p3 = Product(103, "EarPhones", "Sony EarPhones", 899.99, "Electronics", None, True, False)
            p4 = Product(104, "Piano", "Yamaha 88 Keys Acoustic Piano", 54999.99, "Instrument", None, False, True)
            p5 = Product(105, "Laptop", "Dell XPS", "Electronics", 69999.99, None, False, True)
            self._productList.extend([p1, p2, p3, p4, p5])

    def addProduct(self, product):
        if not product in self._productList:
            self._productList.append(product)

    def addProducts(self, *products):
        for each_product in products:
            if not each_product in self._productList:
                self._productList.append(each_product)

    def getProduct(self, productId):
        for each_product in self._productList:
            if each_product.getId() == productId:
                return each_product
    
    def getProducts(self, *productIds):
        products = []
        for each_product_id in productIds:
            for each_product in self._productList:
                if each_product.getId() == each_product_id:
                    products.append(each_product)
                    break
        return products

    def getProductListAdmin(self):
        return self._productList

    def getProductListCustomer(self):
        productListCustomer = []
        for each_product in self._productList:
            if DateUtil.compareDate(each_product.getDateOfExpiry()) and each_product.getInStock():
                productListCustomer.append(each_product)
        return productListCustomer

    def removeProduct(self, productId):
        for each_product in self._productList:
            if each_product.getId() == productId:
                self._productList.remove(each_product)
                break

    def removeProducts(self, *productIds):
        for each_product_id in productIds:
            for each_product in self._productList:
                if each_product.getId() == each_product_id:
                    self._productList.remove(each_product)
                    break


    def updateProduct(self, product):
        for product_index in range(len(self._productList)):
            if self._productList[product_index].getId() == product.getId():
                self._productList[product_index] = product
                break

    def updateProducts(self, *products):
        for each_product in products:
          for product_index in range(len(self._productList)):
              if self._productList[product_index].getId() == each_product.getId():
                  self._productList[product_index] = each_product
                  break