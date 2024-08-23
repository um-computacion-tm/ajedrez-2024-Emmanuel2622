from pieces import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        if self.__color__ == "WHITE":
                return "♙"
        else:
             return "♟"

    def type_move(self, from_row, from_col, to_row, to_col, board):
        if self.__color__ == "WHITE":
            direction = -1
        else:
            direction = 1

        # Validacion movimiento simple hacia adelante
        if from_col == to_col and to_row == from_row + direction:            
            if board.get_piece(to_row, to_col) is None:
                return True
        return False

    def move(self, from_row, from_col, to_row, to_col, board):
        if self.type_move(from_row, from_col, to_row, to_col, board):
            board.__positions__[to_row][to_col] = board.__positions__[from_row][from_col]
            board.__positions__[from_row][from_col] = None
            return True
        else:
            return "Error en el movimiento"