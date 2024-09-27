import unittest
from Game.bishop import Bishop
from Game.pawn import Pawn
from Game.board import *

class Test_Bishop(unittest.TestCase):   
    def setUp(self):
        self.__board__ = Board()
        self.__pawn__white__ = Pawn("WHITE")
        self.__pawn__black__ = Pawn("BLACK")
        self.__bishop__ = Bishop("WHITE")

    def test_move_good(self):
        self.__pawn__white__.move(6, 3, 4, 3, self.__board__)
        self.__pawn__black__.move(1, 0, 3, 0, self.__board__)
        
        result = self.__bishop__.move(7,2,6,3,self.__board__)
        
        self.assertEqual(result, True)
        print(self.__board__.__str__())

    def test_move_good_2(self):
        self.__pawn__white__.move(6, 1, 4, 1, self.__board__)
        self.__pawn__black__.move(1, 0, 3, 0, self.__board__)
        
        result = self.__bishop__.move(7,2,5,0,self.__board__)
        self.assertEqual(result, True)
        print(self.__board__.__str__())

    def test_move_good_3(self):
        self.__pawn__white__.move(6, 0, 4, 0, self.__board__)
        self.__pawn__black__.move(1, 3, 2, 3, self.__board__)
        self.__pawn__white__.move(4, 1, 5, 1, self.__board__)
        
        result = self.__bishop__.move(0,2,3,5,self.__board__)
        self.assertEqual(result, True)
        print(self.__board__.__str__())

    def test_move_bad(self):
        self.__pawn__white__.move(6, 2, 4, 2, self.__board__)
        self.__pawn__black__.move(1, 0, 3, 0, self.__board__)
        
        result = self.__bishop__.move(7,2,6,3,self.__board__)
        self.assertEqual(result, "Error en el movimiento")
        print(self.__board__.__str__())

    def test_move_bad_2(self):
        self.__pawn__white__.move(6, 2, 4, 2, self.__board__)
        self.__pawn__black__.move(1, 0, 3, 0, self.__board__)
        
        result = self.__bishop__.move(7,2,5,4,self.__board__)
        self.assertEqual(result, "Error en el movimiento")
        print(self.__board__.__str__())


    def test_move_bad_3(self):
        self.__pawn__white__.move(6, 2, 4, 2, self.__board__)
        self.__pawn__black__.move(1, 0, 3, 0, self.__board__)
        
        result = self.__bishop__.move(7,2,3,4,self.__board__)
        self.assertEqual(result, "Error en el movimiento")
        print(self.__board__.__str__())
        
    def test_atack(self):
        self.__pawn__white__.move(6, 3, 4, 3, self.__board__)
        self.__pawn__black__.move(1, 7, 2, 7, self.__board__)
        
        result = self.__bishop__.move(7,2,2,7,self.__board__)
        self.assertEqual(result, True)
        print(self.__board__.__str__())
        
if __name__ == "__main__":
    unittest.main()