from pieces import Piece

class Knight(Piece):
    white_str = "♘"
    black_str = "♞"

    def __init__(self, color):
        """
        Inicializa un objeto de tipo Knight (caballo) con un color específico.

        Args:
            color (str): El color de la pieza, puede ser 'WHITE' o 'BLACK'.
        """
        super().__init__(color)

    def type_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento del caballo es válido.

        El caballo se mueve en forma de 'L', lo que significa que se mueve dos casillas en una dirección 
        (horizontal o vertical) y luego una casilla en una dirección perpendicular. 

        Args:
            from_row (int): Fila de origen del caballo.
            from_col (int): Columna de origen del caballo.
            to_row (int): Fila de destino del caballo.
            to_col (int): Columna de destino del caballo.
            board (Board): El tablero que contiene todas las piezas.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        # Verifica el movimiento en forma de 'L'
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            # Verifica que no haya una pieza del mismo color en la casilla de destino
            if not self.is_same_color(from_row, from_col, to_row, to_col, board):
                return True
        return False
