import unittest

import unittest.test
from king import King
from pawn import Pawn
from board import Board

class Test_King(unittest.TestCase):
    def test_move_vertical_good(self):
        self.__board__= Board()
        self.__king__ = King("WHITE")
        self.__pawn_white__ = Pawn("WHITE")
        self.__pawn_black__ = Pawn("BLACK")

        self.__pawn_white__.move(6,4,4,4,self.__board__)
        self.__pawn_black__.move(1,0,2,0,self.__board__)
        
        result = self.__king__.move(7,4,6,4, self.__board__)
        self.assertEqual(result, True)
        print(self.__board__.__str__())

    def test_move_horizontal_good(self):
        self.__board__= Board()
        self.__king__ = King("WHITE")
        self.__pawn_white__ = Pawn("WHITE")
        self.__pawn_black__ = Pawn("BLACK")

        self.__pawn_white__.move(6,4,4,4,self.__board__)
        self.__pawn_black__.move(1,0,2,0,self.__board__)
        self.__king__.move(7,4,6,4, self.__board__)
        self.__pawn_black__.move(2,0,3,0,self.__board__)
        self.__king__.move(6,4,5,4, self.__board__)
        self.__pawn_black__.move(3,0,4,0,self.__board__)

        result = self.__king__.move(5,4,5,3, self.__board__)
        self.assertEqual(result, True)
        print(self.__board__.__str__())

    def test_move_diagonal(self):
        self.__board__= Board()
        self.__king__ = King("WHITE")
        self.__pawn_white__ = Pawn("WHITE")
        self.__pawn_black__ = Pawn("BLACK")

        self.__pawn_white__.move(6,3,4,3,self.__board__)
        self.__pawn_black__.move(1,0,2,0,self.__board__)

        result = self.__king__.move(7,4,6,3, self.__board__)
        self.assertEqual(result, True)
        print(self.__board__.__str__())

    def test_move_vertical_bad(self):
        self.__board__= Board()
        self.__king__ = King("WHITE")

        result = self.__king__.move(7,4,6,3, self.__board__)
        self.assertEqual(result, "Error en el movimiento")
        print(self.__board__.__str__())


    def test_move_horizontal_bad(self):
        self.__board__= Board()
        self.__king__ = King("WHITE")

        result = self.__king__.move(7,4,7,3, self.__board__)
        self.assertEqual(result, "Error en el movimiento")
        print(self.__board__.__str__())

    
    def test_move_diagonal(self):
        self.__board__= Board()
        self.__king__ = King("WHITE")
        self.__pawn_white__ = Pawn("WHITE")
        self.__pawn_black__ = Pawn("BLACK")

        self.__pawn_white__.move(6,3,4,3, self.__board__)
        self.__pawn_black__.move(1,0,2,0, self.__board__)

        result = self.__king__.move(7,4,5,2, self.__board__)
        self.assertEqual(result, "Error en el movimiento")
        print(self.__board__.__str__())

    
if __name__ == "__main__":
    unittest.main()