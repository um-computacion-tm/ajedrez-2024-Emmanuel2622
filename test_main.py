import unittest
from unittest.mock import patch
from main import *
from chess import Chess


class TestPlay(unittest.TestCase):
    
    
    def test_play(self):
        with patch('builtins.input', side_effect=[9,5,4,1]):
            chess = Chess()
            result = play(chess)
            self.assertEqual(result, "El valor from row debe ser mayor a 0 y menor a 7, vuelva a intentar")
    
    def test_play2(self):
        with patch('builtins.input', side_effect=[6,3,"a",5]):
            chess = Chess()
            result = play(chess)
            self.assertEqual(result, "error")

    def test_play3(self):
        with patch('builtins.input', side_effect=[2,3,4,5]):
            chess = Chess()
            result = play(chess)
            self.assertEqual(result, "pass")

    def test_play4(self):
        with patch('builtins.input', side_effect=[1,8,2,3]):
            chess = Chess()
            result = play(chess)
            self.assertEqual(result, "El valor from col debe ser mayor a 0 y menor a 7, vuelva a intentar")
    
    def test_play5(self):
        with patch('builtins.input', side_effect=[2,3,9,3]):
            chess = Chess()
            result = play(chess)
            self.assertEqual(result, "El valor to row debe ser mayor a 0 y menor a 7, vuelva a intentar")

    def test_play6(self):
        with patch('builtins.input', side_effect=[6,2,3,9]):
            chess = Chess()
            result = play(chess)
            self.assertEqual(result, "El valor to col debe ser mayor a 0 y menor a 7, vuelva a intentar")
if __name__ == '__main__':
    unittest.main()