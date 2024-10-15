class Piece:
    def __init__(self, color):
        """
        Inicializa una pieza de ajedrez con el color especificado.

        Args:
            color (str): El color de la pieza (puede ser 'WHITE' o 'BLACK').
        """
        self.__color__ = color

    def __str__(self):
        """
        Retorna la representación de la pieza en forma de string según su color.

        Returns:
            str: La cadena de texto que representa la pieza según su color.
        """
        return self.white_str if self.__color__ == "WHITE" else self.black_str

    def is_same_color(self, from_row, from_col, to_row, to_col, board):
        """
        Comprueba si la pieza en la posición destino es del mismo color que la pieza en la posición de origen.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            to_row (int): Fila de la posición destino.
            to_col (int): Columna de la posición destino.
            board (Board): Instancia del tablero de juego.

        Returns:
            bool: True si ambas piezas son del mismo color, False en caso contrario.
        """
        piece_to = board.get_piece(to_row, to_col)
        piece_from = board.get_piece(from_row, from_col)
        if piece_to is not None:
            if piece_from.__color__ == piece_to.__color__:
                return True
        return False

    def validate_path_is_clean(self, row, col, board):
        if board.get_piece(row, col) is not None:
                return False
        return True
    def get_step(self):
        ...
    def get_iteration(self, target, dest, step):
        for coord in range(target + step, dest, step):
            yield coord

    def clear_path(self, a, b, c, board, direction):
        if direction == "h":
            step = 1 if c > b else -1
            for coord in self.get_iteration(target=b, dest=c, step=step):
                if not self.validate_path_is_clean(a, coord, board):
                    return False
                
        if direction == "v":
            step = 1 if c > a else -1
            for coord in self.get_iteration(target=a, dest=c, step=step):
                if not self.validate_path_is_clean(coord, b, board):
                    return False
        return True
        
    # def clear_horizontal_path(self, from_row, from_col, to_col, board):
    #     step = 1 if to_col > from_col else -1
    #     for col in range(from_col + step, to_col, step):
    #         if not self.validate_path_is_clean(from_row, col, board):
    #             return False
    #     return True

    # def clear_vertical_path(self, from_row, from_col, to_row, board):

    #     step = 1 if to_row > from_row else -1
    #     for coord in self.get_iteration(target=from_row, dest=to_row, step=step):
    #         if not self.validate_path_is_clean(coord, from_col, board):
    #             return False
    #     return True

    def clear_diagonal_path(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el camino diagonal entre la posición de origen y destino está despejado.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            to_row (int): Fila de la posición destino.
            to_col (int): Columna de la posición destino.
            board (Board): Instancia del tablero de juego.

        Returns:
            bool: True si el camino está despejado, False si hay una pieza en el camino.
        """
        row_step = 1 if to_row > from_row else -1
        col_step = 1 if to_col > from_col else -1
        row, col = from_row + row_step, from_col + col_step
        while row != to_row and col != to_col:
            if board.get_piece(row, col) is not None:
                return False
            row += row_step
            col += col_step
        return True

    def move(self, from_row, from_col, to_row, to_col, board):
        """
        Realiza el movimiento de una pieza en el tablero si el movimiento es válido.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            to_row (int): Fila de la posición destino.
            to_col (int): Columna de la posición destino.
            board (Board): Instancia del tablero de juego.

        Returns:
            bool or str: True si el movimiento fue exitoso, 'Error en el movimiento' si fue inválido.
        """
        if self.type_move(from_row, from_col, to_row, to_col, board):
            board.__positions__[to_row][to_col] = board.__positions__[from_row][from_col]
            board.__positions__[from_row][from_col] = None            
            return True
        return "Error en el movimiento"
