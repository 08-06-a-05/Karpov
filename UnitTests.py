import unittest
from zaprosi import *

class DBTest(unittest.TestCase):
    def setUpClass(cls) -> None:
        self.connection=DD