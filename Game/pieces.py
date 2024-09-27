class Piece:
    def __init__(self, color):
        self.__color__ = color

    def __str__(self):
        return self.white_str if self.__color__ == "WHITE" else self.black_str

    def is_same_color(self, from_row, from_col, to_row, to_col, board):
        """Comprueba si la pieza en la posición objetivo es del mismo color."""
        piece_to = board.get_piece(to_row, to_col)
        piece_from = board.get_piece(from_row, from_col)
        if piece_to is not None:
            if piece_from.__color__ == piece_to.__color__:
                return True
        return False
        
    def clear_path(self, from_row, from_col, to_row, to_col, board):
        """Verifica que no haya piezas en el camino."""
        piece = board.get_piece(from_row, from_col)
        if from_row == to_row and piece.__horizontal__:  # Movimiento horizontal
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if board.get_piece(from_row, col) is not None:
                    return False
            return True

        elif to_col == from_col and piece.__vertical__:  # Movimiento vertical
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if board.get_piece(row, from_col) is not None:
                    return False
            return True
        
        elif abs(to_row - from_row) == abs(to_col - from_col) and piece.__diagonal__:  # Movimiento diagonal
            row_step = 1 if to_row > from_row else -1
            col_step = 1 if to_col > from_col else -1
            row, col = from_row + row_step, from_col + col_step
            while row != to_row and col != to_col:
                if board.get_piece(row, col) is not None:
                    return False
                row += row_step
                col += col_step
            return True
        return False
        
    def move(self, from_row, from_col, to_row, to_col, board):        
        if self.type_move(from_row, from_col, to_row, to_col, board):
            board.__positions__[to_row][to_col] = board.__positions__[from_row][from_col]
            board.__positions__[from_row][from_col] = None            
            return True
        return "Error en el movimiento"

