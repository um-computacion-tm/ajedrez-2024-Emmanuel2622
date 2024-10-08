import unittest
from chess import *
from board import *
from pawn import Pawn

class Test_Chess(unittest.TestCase):
    def setUp(self):
        self.__chess__ = Chess()
        self.__board__ = Board()

    def test_move_from_col(self):        
        result = self.__chess__.move(0, 8, 0, 0)
        self.assertEqual(result, "error: La posicion indicada se encuentra fuera del tablero")

    def test_move_to_col(self):
        result = self.__chess__.move(3, 4, 1, -6)
        self.assertEqual(result, "error: La posicion indicada se encuentra fuera del tablero")

    def test_move_from_row(self):
        result = self.__chess__.move(9, 2, 0, 0)
        self.assertEqual(result, "error: La posicion indicada se encuentra fuera del tablero")

    def test_move_to_row(self):
        result = self.__chess__.move(5, 2, 9, 0)
        self.assertEqual(result, "error: La posicion indicada se encuentra fuera del tablero")

    def test_move_pass(self):
        self.__chess__.move(6, 0, 5, 0)
        result = self.__chess__.turn
        self.assertEqual(result, "BLACK")

    def test_move_valor_no_numerico(self):
        result = self.__chess__.move(0, "hola", 0, 0)
        self.assertEqual(result, "error: Valor no Numerico")    

    def test_change_turn_black(self):
        result = self.__chess__.change_turn()
        self.__chess__.__turn__ = "WHITE"
        self.assertEqual(result, "BLACK")

    def test_change_turn_white(self):
        self.__chess__.change_turn()
        result = self.__chess__.change_turn()
        self.__chess__.__turn__ = "BLACK"
        self.assertEqual(result, "WHITE")

    def test_move_no_hay_pieza(self):
        result = self.__chess__.move(4, 0, 5, 0)
        self.assertEqual(result, "error: La posicion esta vacia")

    def test_move_turno_incorrecto(self):
        result = self.__chess__.move(1, 0, 2, 0)
        self.assertEqual(result, "error: No puede mover una pieza de otro jugador")
    
    def test_move_piece_pawn_invalid(self):
        result = self.__chess__.move(6, 0, 5, 3)
        self.assertEqual(result, "error: Movimiento de pieza Invalido")

    def test_game_over(self):
        self.__chess__.__game_over__ = True 
        result = self.__chess__.move(0, 0, 1, 1)
        self.assertEqual(result, "La partida ha terminado.")

if __name__ == "__main__":
    unittest.main()
