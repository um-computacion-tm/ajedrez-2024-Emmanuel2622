from pieces import Piece

class King(Piece):
    white_str = "♔"
    black_str = "♚"

    #Movimiento Vertical y Horizontal
    def type_move(self, from_row, from_col, to_row, to_col, board):

        if self.color_igual(from_row, from_col, to_row, to_col, board):
            if abs(from_row - to_row) == 1 or (from_col - to_col) == 1:
                return True
        return False