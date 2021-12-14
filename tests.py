import unittest

import sqlite3


class DB():
    def __init__(self):
        self.connection = sqlite3.connect('NewDB.db')

    def CursorOpen(self):
        self.cursor = self.connection.cursor()

    def CursorClose(self):
        self.cursor.close()

    def close(self):
        self.connection.close()

    def Renault_cars(self):
        self.cursor.execute('SELECT id_car FROM cars WHERE brand=(SELECT id FROM brands WHERE name="Renault")')
        return self.cursor.fetchall()

    def BMW_X5_choosers(self):
        self.cursor.execute(
            'SELECT name_of_customer AS "Имя клиента",phone AS "Телефон клиента" FROM orders WHERE id_car=(SELECT '
            'id_car '
            'FROM cars WHERE brand=(SELECT id FROM brands WHERE name="BMW") AND model="X5")')
        return self.cursor.fetchall()

    def BMW_X5_without_discounts(self):
        self.cursor.execute(
            'SELECT name_of_customer AS "Имя клиента",phone AS "Телефон клиента" FROM orders WHERE status="Интересовался" '
            'AND best_price>=10000000000 AND id_car=(SELECT id_car FROM cars where brand=(SELECT id from brands where '
            'name="BMW") and model="X5")')
        return self.cursor.fetchall()


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
