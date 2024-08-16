import unittest
from chess import *

class Test_Chess(unittest.TestCase):
    def setUp(self):
        self.__chess__ = Chess()

    def test_move(self):        
        result = self.__chess__.move(0,8,0,0)
        print(result)
        self.assertEqual(
            result, "error value"
        )

    def test_move2(self):
        result = self.__chess__.move(0,2,0,0)
        print(result)
        self.assertEqual(
            result, "pass"
        )

    def test_move3(self):
        result = self.__chess__.move(0,9,0,0)
        print(result)
        self.assertEqual(
            result, "error value"
        )

    def test_turn(self):
        result = self.__chess__.turn
        print(result)
        self.assertEqual(
            result, "WHITE"
        )
if __name__ == "__main__":
    unittest.main()