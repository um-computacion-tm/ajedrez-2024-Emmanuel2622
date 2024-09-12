class Piece:
    def __init__(self, color):
        self.__color__ = color

    def move(self, from_row, from_col, to_row, to_col, board):
        if self.type_move(from_row, from_col, to_row, to_col, board):
            board.__positions__[to_row][to_col] = board.__positions__[from_row][from_col]
            board.__positions__[from_row][from_col] = None
            return True
        else:
            return "Error en el movimiento"