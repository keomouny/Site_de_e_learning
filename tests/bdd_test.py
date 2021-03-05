import unittest
from bdd import BDD


class BddTest(unittest.TestCase, BDD):

    def test_class_init(self):
        bddee = BDD()
        self.assertTrue(isinstance(bddee, BDD))
