class Piece:
    def __init__(self, color):
        self.__color__ = color

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
    
    def color_igual(self, from_row, from_col,to_row, to_col, board):
        """Comprueba si la pieza en la posición objetivo es del mismo color."""
        piece_to_color = board.get_piece(to_row, to_col)
        piece_from_color = board.get_piece(from_row, from_col)
        if piece_to_color is not None and piece_from_color.__color__ == piece_to_color.__color__:
            print("false")
            return False
        return True
    
    def move(self, from_row, from_col, to_row, to_col, board):
        if self.type_move(from_row, from_col, to_row, to_col, board):
            board.__positions__[to_row][to_col] = board.__positions__[from_row][from_col]
            board.__positions__[from_row][from_col] = None
            return True
        else:
            return "Error en el movimiento"
    