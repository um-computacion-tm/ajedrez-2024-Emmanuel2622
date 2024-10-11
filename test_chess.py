import unittest
from chess import *
from board import *

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
        self.assertEqual(result, "error: Valor no Numérico")

    def test_change_turn_black(self):
        result = self.__chess__.change_turn()
        self.assertEqual(result, "BLACK")

    def test_change_turn_white(self):
        self.__chess__.change_turn()  # Cambia a BLACK
        result = self.__chess__.change_turn()  # Debería cambiar de nuevo a WHITE
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
        result = self.__chess__.move(6, 0, 5, 0)
        self.assertIsNone(result)

    def test_request_draw_white(self):
        result = self.__chess__.request_draw()
        self.assertEqual(result, "Esperando a que ambos jugadores estén de acuerdo.")
        self.assertTrue(self.__chess__.__white_agrees__)

    def test_request_draw_black(self):
        self.__chess__.change_turn()
        result = self.__chess__.request_draw()
        self.assertEqual(result, "Esperando a que ambos jugadores estén de acuerdo.")
        self.assertTrue(self.__chess__.__black_agrees__)

    def test_draw_agreement(self):
        result = self.__chess__.request_draw()  
        self.assertEqual(result, "Esperando a que ambos jugadores estén de acuerdo.")

        self.__white_agrees__ = True
        self.__black_agrees__ = True
        result = self.__chess__.request_draw()  
        self.assertEqual(result, "La partida ha terminado en empate.")

    def test_check_game_over_white_wins(self):
        for row in self.__chess__.__board__.__positions__:
            for col in range(len(row)):
                piece = row[col]
                if piece is not None and piece.__color__ == "BLACK":
                    row[col] = None
        result = self.__chess__.check_game_over()
        self.assertTrue(result)

    def test_check_game_over_black_wins(self):
        # Vaciar todas las piezas blancas para simular la victoria de las negras
        for row in self.__chess__.__board__.__positions__:
            for col in range(len(row)):
                piece = row[col]
                if piece is not None and piece.__color__ == "WHITE":
                    row[col] = None
        result = self.__chess__.check_game_over()
        self.assertTrue(result)
if __name__ == "__main__":
    unittest.main()
