import unittest
from board import *

class Test_Board(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_board_pos_1(self):
        piece = self.board.get_piece(0, 0)
        self.assertEqual(piece.__color__, "BLACK")
    
    def test_board_pos_2(self):
        piece = self.board.get_piece(0, 7)
        self.assertEqual(piece.__color__, "BLACK")
    
    def test_board_pos_2(self):
        piece = self.board.get_piece(7, 7)
        self.assertEqual(piece.__color__, "WHITE")
    
    def test_board_pos_1(self):
        piece = self.board.get_piece(7, 0)
        self.assertEqual(piece.__color__, "WHITE")
    
if __name__ == "__main__":
    unittest.main()
