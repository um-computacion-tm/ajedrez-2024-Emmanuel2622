import unittest
from chess import *

class Test_Chess(unittest.TestCase):
    def setUp(self):
        self.__chess__ = Chess()

    def test_move_from_col(self):        
        result = self.__chess__.move(0,8,0,0)
        print(result)
        self.assertEqual(
            result, "Error value from_col, out range"
        )

    def test_move_to_col(self):
        result = self.__chess__.move(3,4,1,-6)
        print(result)
        self.assertEqual(
            result, "Error value to_col, out range"
        )

    def test_move_from_row(self):
        result = self.__chess__.move(9,2,0,0)
        print(result)
        self.assertEqual(
            result, "Error value from_row, out range"
        )

    def test_move_to_row(self):
        result = self.__chess__.move(5,2,9,0)
        print(result)
        self.assertEqual(
            result, "Error value to_row, out range"
        )

    def test_move_pass(self):
        result = self.__chess__.move(0,2,0,0)
        print(result)
        self.assertEqual(
            result, "pass"
        )

    def test_move_valor_no_numerico(self):
        result = self.__chess__.move(0,"hola",0,0)
        print(result)
        self.assertEqual(
            result, "error: no se ingreso un valor numerico"
        )    

    def test_turn(self):
        result = self.__chess__.turn
        print(result)
        self.assertEqual(
            result, "WHITE"
        )

    def test_change_turn_black(self):
        result = self.__chess__.change_turn()
        self.__chess__.__turn__ = "WHITE"
        print(result)
        self.assertEqual(
            result, "BLACK"
        )

    def test_change_turn_white(self):
        self.__chess__.change_turn()

        result = self.__chess__.change_turn()
        self.__chess__.__turn__ = "BLACK"
        print(result)
        self.assertEqual(
            result, "WHITE"
        )

if __name__ == "__main__":
    unittest.main()