from rook import Rook
from pawn import Pawn
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from exceptions import *
class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        
        # Colocar las piezas en las posiciones iniciales
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][7] = Rook("WHITE")
        self.__positions__[7][0] = Rook("WHITE")
        
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")
            self.__positions__[6][i] = Pawn("WHITE")
        
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[7][6] = Knight("WHITE")
        self.__positions__[7][1] = Knight("WHITE")

        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[7][5] = Bishop("WHITE")
        self.__positions__[7][2] = Bishop("WHITE")

        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")
    
    def __str__(self):
        """
        Devuelve una representación en cadena del tablero de ajedrez con los números de filas y columnas.
        """
        board_str = "  0 1 2 3 4 5 6 7\n"  # Números de columna en la parte superior
        for i, row in enumerate(self.__positions__):
            board_str += f"{i} "  # Número de fila al comienzo de cada línea
            for cell in row:
                if cell is not None:
                    board_str += f"{str(cell)} "  # Espacio para mejor legibilidad
                else:
                    board_str += ". "  # Poner un punto para las celdas vacías
            board_str += f"{i}\n"  # Número de fila al final de cada línea para simetría
        board_str += "  0 1 2 3 4 5 6 7\n"  # Números de columna en la parte inferior
        return board_str


    def get_piece(self, row, col):
        """
        Devuelve la pieza en una posición dada del tablero.

        Args:
            row (int): Fila de la pieza.
            col (int): Columna de la pieza.

        Returns:
            Pieza: Objeto de pieza o None si la posición está vacía.
        """
        if row < 0 or col < 0:
            raise OutOfBoard
        try:
            return self.__positions__[row][col]
        except IndexError:
            raise OutOfBoard