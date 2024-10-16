from pieces import Piece

class Bishop(Piece):
    """
    Clase que representa el alfil en ajedrez.

    El alfil se mueve exclusivamente en diagonal y no puede saltar sobre otras piezas. 
    Su movimiento es ilimitado en cuanto a la cantidad de casillas, siempre que se mantenga en una misma diagonal.
    """

    white_str = "♗"
    black_str = "♝"

    def type_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento del alfil es válido.

        El alfil se mueve en diagonal en cualquier dirección, pero no puede atravesar otras piezas.
        Además, no puede capturar piezas del mismo color.

        Args:
            from_row (int): Fila de origen del alfil.
            from_col (int): Columna de origen del alfil.
            to_row (int): Fila de destino del alfil.
            to_col (int): Columna de destino del alfil.
            board (Board): El tablero que contiene todas las piezas.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        # Verificar que no es la misma posición ni hay una pieza del mismo color en la posición destino
        if self.is_same_color(from_row, from_col, to_row, to_col, board):
            return False
        # El alfil se mueve en diagonal: la diferencia entre filas debe ser igual a la de columnas
        if self.clear_diagonal_path(from_row, from_col, to_row, to_col, board):
            return True