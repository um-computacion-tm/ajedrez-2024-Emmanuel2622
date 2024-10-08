import unittest
from rook import *
from pawn import *
from board import *

class Test_Rook(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()  
        self.__rook__ = Rook("WHITE")
        self.__pawn_white__ = Pawn("WHITE")
        self.__pawn_black__ = Pawn("BLACK")

        self.__pawn_white__.move(6,0,5,0,self.__board__)
        self.__pawn_black__.move(1,1,2,1,self.__board__)
        self.__pawn_white__.move(5,0,4,0,self.__board__)

    def test_move_vertical_good(self):
        self.__pawn_black__.move(2,1,3,1,self.__board__)
        self.__pawn_white__.move(4,0,3,1,self.__board__)
        self.__pawn_black__.move(1,0,2,0,self.__board__)
        
        result = self.__rook__.move(7,0,2,0, self.__board__)
        self.assertEqual(result, True)

    def test_move_horizontal_good(self):
        self.__pawn_black__.move(2,1,3,1,self.__board__)
        self.__pawn_white__.move(4,0,3,1,self.__board__)
        self.__pawn_black__.move(1,0,2,0,self.__board__)
        self.__rook__.move(7,0,5,0, self.__board__)
        
        result = self.__rook__.move(5,0,5,2, self.__board__)
        self.assertEqual(result, True)

    def test_move_vertical_bad(self):
        self.__pawn_black__.move(2,1,3,1,self.__board__)
        self.__pawn_white__.move(4,0,3,1,self.__board__)
        self.__pawn_black__.move(1,0,2,0,self.__board__)
        
        result = self.__rook__.move(0,0,4,0, self.__board__)
        self.assertEqual(result, 'Error en el movimiento')


    def test_move_horizontal_bad(self):
        self.__pawn_black__.move(1,0,2,0,self.__board__)
        self.__pawn_white__.move(6,1,5,1,self.__board__)
        self.__pawn_black__.move(1,1,2,1,self.__board__)
        self.__rook__.move(7,0,5,0, self.__board__)
        self.__pawn_black__.move(2,1,3,1,self.__board__)

        result = self.__rook__.move(5,0,5,3, self.__board__)
        self.assertEqual(result, 'Error en el movimiento')

    def test_is_same_color(self):
        result = self.__rook__.move(7,0,7,1, self.__board__)
        self.assertEqual(result, 'Error en el movimiento')
if __name__ == "__main__":
    unittest.main()
