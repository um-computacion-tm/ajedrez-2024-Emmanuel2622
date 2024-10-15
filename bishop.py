from pieces import Piece

class Bishop(Piece):
    white_str = "♗"
    black_str = "♝"
    horizontal = False
    vertical = False
    diagonal = True

    def type_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento es válido para el alfil. El alfil solo se mueve en diagonal,
        y no puede moverse sobre piezas de su mismo color.

        Args:
            from_row (int): Fila de origen de la pieza.
            from_col (int): Columna de origen de la pieza.
            to_row (int): Fila de destino de la pieza.
            to_col (int): Columna de destino de la pieza.
            board (Board): El tablero que contiene todas las piezas.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        # Verificar que no es la misma posición ni hay una pieza del mismo color en la posición destino
        if not self.is_same_color(from_row, from_col, to_row, to_col, board):
            # El alfil se mueve en diagonal, por lo que la diferencia en filas debe ser igual a la de columnas
            if abs(to_row - from_row) == abs(to_col - from_col):
                # Verificar si el camino está despejado para el movimiento
                return self.clear_path(from_row, from_col, to_row, to_col, board)
        return False

