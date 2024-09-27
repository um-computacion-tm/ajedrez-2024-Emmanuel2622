import unittest
from Game.pawn import Pawn
from Game.board import *

class Test_Pawn(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()        
        

    def test_salto_simple_adelante(self):
        self.__pawn__ = Pawn("WHITE")
        
        result = self.__pawn__.move(6,0,5,0, self.__board__)
        print(result)
        self.assertEqual(
            result, True
            )

    def test_salto_simple_vertical(self):
        self.__pawn__ = Pawn("WHITE")
        
        result = self.__pawn__.move(6,0,5,1, self.__board__)
        print(result)
        self.assertEqual(
            result, "Error en el movimiento"
            )

    def test_salto_simple_atras(self):
        self.__pawn__ = Pawn("WHITE")
        
        result = self.__pawn__.move(6,0,7,0, self.__board__)
        print(result)
        self.assertEqual(
            result, "Error en el movimiento"
            )
        
    def test_salto_simple_adelante_negro(self):
        self.__pawn__ = Pawn("BLACK")
        
        result = self.__pawn__.move(1,0,2,0, self.__board__)
        print(result)
        self.assertEqual(
            result, True
            )
        
    def test_salto_simple_vertical_negro(self):
        self.__pawn__ = Pawn("BLACK")
        
        result = self.__pawn__.move(1,0,2,1, self.__board__)
        print(result)
        self.assertEqual(
            result, "Error en el movimiento"
            )

    def test_salto_simple_atras_negro(self):
        self.__pawn__ = Pawn("BLACK")
        
        result = self.__pawn__.move(1,0,0,0, self.__board__)
        print(result)
        self.assertEqual(
            result, "Error en el movimiento"
            )
    
    def test_salto_doble_adelante(self):
        self.__pawn__ = Pawn("WHITE")
        self.__pawn__.__first_move__ = True

        result = self.__pawn__.move(6,0,4,0, self.__board__)
        print(result)
        self.assertEqual(
            result, True
        )

    def test_salto_doble_adelante_no_first_move(self):
        self.__pawn__ = Pawn("WHITE")
        self.__pawn__.__first_move__ = True
        self.__pawn__.move(6,0,4,0, self.__board__)
        
        self.__pawn__.__first_move__ = False
        result = self.__pawn__.move(4,0,2,0, self.__board__)
        print(result)
        self.assertEqual(
            result, "Error en el movimiento"
        )
    
    def test_salto_doble_adelante_negro(self):
        self.__pawn__ = Pawn("BLACK")
        self.__pawn__.__first_move__ = True

        result = self.__pawn__.move(1,3,3,3, self.__board__)
        print(result)
        self.assertEqual(
            result, True
        )

    def test_salto_doble_adelante_no_first_move_negro(self):
        self.__pawn__ = Pawn("BLACK")
        self.__pawn__.__first_move__ = True
        self.__pawn__.move(1,6,2,6, self.__board__)
        
        self.__pawn__.__first_move__ = False
        result = self.__pawn__.move(2,6,4,6, self.__board__)
        print(result)
        self.assertEqual(
            result, "Error en el movimiento"
        )
    
    def test_ataque_diagonal(self):
        self.__pawn_black__ = Pawn("BLACK")
        self.__pawn__white__ = Pawn("WHITE")

        self.__pawn_black__.move(1,6,3,6, self.__board__)

        self.__pawn__white__.move(6,5,4,5, self.__board__)
        result = self.__pawn__white__.move(4,5,3,6, self.__board__)
        print(result)
        self.assertEqual(
            result, True
            )

    def test_ataque_diagonal_fallo(self):
        self.__pawn_white_2__ = Pawn("WHITE")
        self.__pawn__white__ = Pawn("WHITE")

        self.__pawn_white_2__.move(6,6,4,6, self.__board__)

        self.__pawn__white__.move(6,5,5,5, self.__board__)
        result = self.__pawn__white__.move(5,5,4,6, self.__board__)
        
        print(result)
        self.assertEqual(
            result, "Error en el movimiento"
            )

if __name__ == "__main__":
    unittest.main()
