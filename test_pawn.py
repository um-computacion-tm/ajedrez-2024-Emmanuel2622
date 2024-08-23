import unittest
from pawn import Pawn
from board import *

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
    
if __name__ == "__main__":
    unittest.main()
