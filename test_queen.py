import unittest
from queen import Queen
from pawn import Pawn
from board import *

class Test_Queen(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()
        self.__pawn_white__ = Pawn("WHITE")
        self.__pawn_black__ = Pawn("BLACK")
        self.__Queen__ = Queen("WHITE")
        self.__pawn_white__.move(6,3,4,3, self.__board__)

    def test_move_vertical_good(self):

        result = self.__Queen__.move(7,3,6,3, self.__board__)
        self.assertEqual(result, True)
        

    def test_move_horizontal_good(self):
        self.__Queen__.move(7,3,5,3, self.__board__)
        
        result = self.__Queen__.move(5,3,5,1, self.__board__)
        self.assertEqual(result, True)
        

    def test_move_vertical_2_good(self):
        self.__Queen__.move(7,3,5,3, self.__board__)

        result = self.__Queen__.move(5,3,7,3, self.__board__)
        self.assertEqual(result, True)
        

    def test_move_horizontal_2_good(self):
        self.__Queen__.move(7,3,5,3, self.__board__)
        
        result = self.__Queen__.move(5,3,5,6, self.__board__)
        self.assertEqual(result, True)
        

    def test_move_diagonal_good(self):
        self.__Queen__.move(7,3,5,3, self.__board__)
        
        result = self.__Queen__.move(5,3,2,2, self.__board__)
        self.assertEqual(result, True)

    def test_move_vertical_bad(self):

        result = self.__Queen__.move(7,3,3,3, self.__board__)
        self.assertEqual(result, "Error en el movimiento")
        

    def test_move_horizontal_bad(self):
        self.__Queen__.move(7,3,5,3, self.__board__)
        self.__pawn_white__.move(6,4,5,4, self.__board__)
        
        result = self.__Queen__.move(5,3,5,7, self.__board__)
        self.assertEqual(result, "Error en el movimiento")
        
    def test_move_diagonal_bad(self):
        self.__Queen__.move(7,3,6,3, self.__board__)
        self.__pawn_white__.move(6,4,5,4, self.__board__)
        
        result = self.__Queen__.move(6,3,4,5, self.__board__)
        self.assertEqual(result, "Error en el movimiento")
    
    def test_move_diagonal_bad2(self):
        
        result = self.__Queen__.move(7,3,7,2, self.__board__)
        self.assertEqual(result, "Error en el movimiento")
    