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
                "♜♞♝♛♚♝♞♜\n"

                "♟♟♟♟♟♟♟♟\n"

                "        \n"

                "        \n"

                "        \n"

                "        \n"

                "♙♙♙♙♙♙♙♙\n"

                "♖♘♗♕♔♗♘♖\n"
            )
        )
    
if __name__ == "__main__":
    unittest.main()