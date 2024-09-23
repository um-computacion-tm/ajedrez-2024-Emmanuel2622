from pieces import Piece

class Rook(Piece):
    white_str = "♖"
    black_str = "♜"

    def __init__(self, color):
        super().__init__(color)

    def type_move(self, from_row, from_col, to_row, to_col, board):
        if self.is_same_color(from_row, from_col, to_row, to_col, board):
            return False
        return self.clear_path(from_row, from_col, to_row, to_col, board)