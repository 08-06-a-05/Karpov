import unittest

class DBTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.baza = DB()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.baza.close()

    def setUp(self) -> None:
        self.baza.CursorOpen()

    def tearDown(self) -> None:
        self.baza.CursorClose()

    def testRenaultCars(self):
        self.assertEqual([(1,)],self.baza.Renault_cars())

    def testBmwX5Choosers(self):
        self.assertEqual([('Никита', '+79999999999'), ('Наташа', '+78888888888')],self.baza.BMW_X5_choosers())

    def testBmwX5WithoutDiscounts(self):
        self.assertEqual([('Никита', '+79999999999')],self.baza.BMW_X5_without_discounts())

if __name__ == "__main__":
    unittest.main(failfast=False)
