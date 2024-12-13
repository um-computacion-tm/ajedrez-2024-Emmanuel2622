from pieces import Piece

class Knight(Piece):
    """
    Clase que representa la pieza del caballo en el ajedrez.

    El caballo se mueve en forma de 'L', lo que significa que puede moverse dos casillas 
    en una dirección y luego una casilla en una dirección perpendicular, o viceversa.
    Puede saltar sobre otras piezas.
    """

    white_str = "♘"
    black_str = "♞"

    def type_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento del caballo es válido.

        El caballo se mueve en forma de 'L', lo que significa que se mueve dos casillas en una dirección 
        (horizontal o vertical) y luego una casilla en una dirección perpendicular. 
        El caballo también puede saltar sobre otras piezas.

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
