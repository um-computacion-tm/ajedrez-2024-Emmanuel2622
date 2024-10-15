from pieces import Piece

class Rook(Piece):
    white_str = "♖"
    black_str = "♜"

    def type_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento de la torre es válido.

        La torre se puede mover en línea recta, ya sea vertical u horizontal,
        siempre que no haya piezas que bloqueen su camino.

        Args:
            from_row (int): Fila de origen de la torre.
            from_col (int): Columna de origen de la torre.
            to_row (int): Fila de destino de la torre.
            to_col (int): Columna de destino de la torre.
            board (Board): El tablero que contiene todas las piezas.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        # Verifica si el movimiento no es hacia una casilla ocupada por una pieza del mismo color
        if self.is_same_color(from_row, from_col, to_row, to_col, board):
            return False

        # Verifica si hay un camino despejado para el movimiento
        if from_row == to_row:  # Movimiento horizontal
            return self.clear_horizontal_path(from_row, from_col, to_col, board)
        elif to_col == from_col:  # Movimiento vertical
            return self.clear_vertical_path(from_row, to_row, from_col, board)
