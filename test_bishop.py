import unittest
from bishop import Bishop
from pawn import Pawn
from board import *

class Test_Bishop(unittest.TestCase):    
    def test_move_good(self):
        self.__board__ = Board()
        self.__pawn__white__ = Pawn("WHITE")
        self.__pawn__black__ = Pawn("WHITE")
        self.__bishop__ = Bishop("WHITE")

        self.__pawn__white__.move(6, 2, 4, 2, self.__board__)
        self.__pawn__black__.move(1, 0, 3, 0, self.__board__)
        
        result = self.__bishop__.move(7,1,6,2,self.__board__)
        self.assertEqual(result, True)
        print(self.__board__.__str__())


    def test_move_good_2(self):
        self.__board__ = Board()
        self.__pawn__white__ = Pawn("WHITE")
        self.__pawn__black__ = Pawn("WHITE")
        self.__bishop__ = Bishop("WHITE")

        self.__pawn__white__.move(6, 2, 4, 2, self.__board__)
        self.__pawn__black__.move(1, 0, 3, 0, self.__board__)
        
        result = self.__bishop__.move(7,1,5,3,self.__board__)
        self.assertEqual(result, True)
        print(self.__board__.__str__())

    def test_move_bad(self):
        self.__board__ = Board()
        self.__pawn__white__ = Pawn("WHITE")
        self.__pawn__black__ = Pawn("WHITE")
        self.__bishop__ = Bishop("WHITE")

        self.__pawn__white__.move(6, 2, 4, 2, self.__board__)
        self.__pawn__black__.move(1, 0, 3, 0, self.__board__)
        
        result = self.__bishop__.move(7,1,6,3,self.__board__)
        self.assertEqual(result, "Error en el movimiento")
        print(self.__board__.__str__())