import unittest
from board import *


class Test_Board(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        
    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "  0 1 2 3 4 5 6 7\n"
                "0 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 0\n"
                "1 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 1\n"
                "2 . . . . . . . . 2\n"
                "3 . . . . . . . . 3\n"
                "4 . . . . . . . . 4\n"
                "5 . . . . . . . . 5\n"
                "6 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 6\n"
                "7 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 7\n"
                "  0 1 2 3 4 5 6 7\n"
            )
        )   

if __name__ == "__main__":
    unittest.main()