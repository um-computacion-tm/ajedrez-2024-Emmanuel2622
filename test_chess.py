import unittest
from chess import Chess
from board import Board

class TestMove(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()

    def test_move(self):        
        result = self.chess.move(0,8,0,0)
        print(result)
        self.assertEqual(
            result, "El valor debe ser mayor a 0 y menor a 7, vuelva a intentar"
        )

    def test_move2(self):
        result = self.chess.move(0,2,0,0)
        print(result)
        self.assertEqual(
            result, "pass"
        )
if __name__ == "__main__":
    unittest.main()