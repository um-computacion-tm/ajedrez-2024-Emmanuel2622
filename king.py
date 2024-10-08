from pieces import Piece

class King(Piece):
    white_str = "♔"
    black_str = "♚"

    def __init__(self, color):
        """
        Inicializa un objeto de tipo King (rey) con un color específico.

        Args:
            color (str): El color de la pieza, puede ser 'WHITE' o 'BLACK'.
        """
        super().__init__(color)
        self.__horizontal__ = True
        self.__vertical__ = True
        self.__diagonal__ = True

    def type_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento es válido para el rey. El rey se mueve una casilla en cualquier dirección
        (horizontal, vertical o diagonal), siempre que no esté bloqueado por una pieza del mismo color.

        Args:
            from_row (int): Fila de origen del rey.
            from_col (int): Columna de origen del rey.
            to_row (int): Fila de destino del rey.
            to_col (int): Columna de destino del rey.
            board (Board): El tablero que contiene todas las piezas.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        # Verificar si hay una pieza del mismo color en la posición de destino
        if self.is_same_color(from_row, from_col, to_row, to_col, board):
            return False

        # El rey se mueve como máximo una casilla en cualquier dirección
        if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1:
            return True

        return False
