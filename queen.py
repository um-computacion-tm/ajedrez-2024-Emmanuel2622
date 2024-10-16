from pieces import Piece

class Queen(Piece):
    """
    Clase que representa a la reina en el tablero de ajedrez.

    Attributes:
        white_str (str): Representación de la reina blanca en formato de texto.
        black_str (str): Representación de la reina negra en formato de texto.
    """
    white_str = "♕"
    black_str = "♛"

    def type_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento de la reina es válido.

        La reina se puede mover en cualquier dirección (horizontal, vertical o diagonal),
        siempre que el camino esté despejado y que no termine en una casilla ocupada
        por una pieza del mismo color.

        Args:
            from_row (int): Fila de origen de la reina.
            from_col (int): Columna de origen de la reina.
            to_row (int): Fila de destino de la reina.
            to_col (int): Columna de destino de la reina.
            board (Board): El tablero que contiene todas las piezas.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        # Verifica si la casilla destino está ocupada por una pieza del mismo color
        if self.is_same_color(from_row, from_col, to_row, to_col, board):
            return False

        # Verifica si es un movimiento horizontal
        if from_row == to_row:
            return self.clear_path(from_row, from_col, to_col, board, direction="h")
        
        # Verifica si es un movimiento vertical
        elif from_col == to_col:
            return self.clear_path(from_row, from_col, to_row, board, direction="v")
        
        # Verifica si es un movimiento diagonal
        elif abs(to_row - from_row) == abs(to_col - from_col):
            return self.clear_diagonal_path(from_row, from_col, to_row, to_col, board)

        # Si no cumple con ninguno de los movimientos válidos de la reina
        return False