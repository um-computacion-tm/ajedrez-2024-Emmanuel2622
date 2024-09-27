import unittest
from unittest.mock import patch
from Game.cli import *
from Game.chess import Chess


class TestPlay(unittest.TestCase):
    
    @patch(
            'builtins.input',
            side_effect=[9,5,4,1]
            )
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_play1(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
        ):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 1)
    
    @patch(
            'builtins.input',
            side_effect=[6,3,"a",5]
            )
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_play2(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
        ):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 3)
        self.assertEqual(mock_print.call_count, 4)
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch(
            'builtins.input',
            side_effect=[2,3,4,"as"]
            )
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_play3(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
        ):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 4)
        self.assertEqual(mock_chess_move.call_count, 0)

if __name__ == '__main__':
    unittest.main()