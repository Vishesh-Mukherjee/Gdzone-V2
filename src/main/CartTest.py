import unittest
from CartImpl import CartImpl
from CartImpl import CartImpl

class CartTest(unittest.TestCase):

    cartImpl = CartImpl()

    def testGetAllCartItems(self):
        self.assertRaises(Exception, CartImpl.getAllCartItems, 1001)
    
    def testGetCartTotal(self):
        self.assertRaises(Exception, CartImpl.getCartTotal, 1001)
    
    def testAddCartItem(self):
        self.cartImpl.addCartItem(1001, 101)
        self.assertEqual(1, len(self.cartImpl.getAllCartItems(1001)))

    def testRemoveCartItem(self):
        self.cartImpl.removeCartItem(1001, 101)
        self.assertEqual(0, len(self.cartImpl.getAllCartItems(1001)))

cartTest = CartTest()
cartTest.testGetAllCartItems()
cartTest.testGetCartTotal
cartTest.testAddCartItem()
cartTest.testRemoveCartItem()