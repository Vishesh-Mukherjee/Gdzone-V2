import unittest
from ProductInventoryImpl import ProductInventoryImpl
from Product import Product
from DateUtil import DateUtil

class ProductInventoryTest(unittest.TestCase):

    productInventory = ProductInventoryImpl()

    def testGetProductListAdmin(self):
        self.assertEqual(5, len(self.productInventory.getProductListAdmin())) 

    def testGetProductListCustomer(self):
        self.assertEqual(3, len(self.productInventory.getProductListCustomer()))       

    def testAddProduct(self):
        p6 = Product(106, "Tuna Fish", "Fresh Water Tuna Fish", "Food & Beverage", 599.99, DateUtil.stringToDate("29-06-2021"), True, True)
        self.productInventory.addProduct(p6)
        self.assertEqual(6, len(self.productInventory.getProductListAdmin()))
    
    def testAddProducts(self):
        p7 = Product(107, "Chair", "Rosewood Chair", "Furniture", 1499.99, None, False, True)
        p8 = Product(108, "Zara Shirt", "Zara Black Shirt, Size - M", "Fashion & Clothing", 759.99, None, True, False)
        self.productInventory.addProducts(p7, p8)
        self.assertEqual(8, len(self.productInventory.getProductListAdmin()))
    
    def testRemoveProduct(self):
        self.productInventory.removeProduct(108)
        self.assertEqual(7, len(self.productInventory.getProductListAdmin()))

    def testRemoveProducts(self):
        self.productInventory.removeProduct(107, 106)
        self.assertEqual(5, len(self.productInventory.getProductListAdmin()))

    def testUpdateProduct(self):
        p1 = Product(101, "Iphone", "Iphone 11 Max Pro", "Electronics", 89999.99, None, True, True)
        self.productInventory.updateProduct(p1)
        self.assertEqual(p1, self.productInventory.getProduct(101))

    def testUpdateProducts(self):
        p2 = Product(102, "Sandwich", "Cheese Sandwich", "Food & Beverage", 499.99, DateUtil.stringToDate("31-10-2021"), True, True)
        p3 = Product(103, "EarPhones", "Sony EarPhones", 999.99, "Electronics", None, False, False)
        self.productInventory.updateProducts(p2, p3)
        self.assertEqual(p2, self.productInventory.getProduct(102))
        self.assertEqual(p3, self.productInventory.getProduct(103))
 
productInventoryTest = ProductInventoryTest()
productInventoryTest.testGetProductListAdmin()
productInventoryTest.testGetProductListCustomer()
productInventoryTest.testAddProduct()
productInventoryTest.testAddProducts()
productInventoryTest.testRemoveProduct()
productInventoryTest.testUpdateProduct()
productInventoryTest.testUpdateProducts()