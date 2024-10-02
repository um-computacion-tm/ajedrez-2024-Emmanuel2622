import unittest
from knight import Knight
from board import Board

class Test_knight(unittest.TestCase):
    def setUp(self):
        self.__knight__ = Knight("WHITE")
        self.__board__ = Board()

    def test_move_L(self):
        result = self.__knight__.move(7,1,5,2,self.__board__)
        self.assertEqual(result, True)

    def test_move_L_fail(self):
        result = self.__knight__.move(7,1,5,1,self.__board__)
        self.assertEqual(result, "Error en el movimiento")
    
    def test_is_same_color(self):
        result = self.__knight__.move(7,1,6,1,self.__board__)
        self.assertEqual(result, "Error en el movimiento")
        