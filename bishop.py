from pieces import Piece

class Bishop(Piece):
    white_str = "♗"
    black_str = "♝"

    def __init__(self, color):
        super().__init__(color)
    
    def type_move(self, from_row, from_col, to_row, to_col, board):
        if not self.is_same_color(from_row, from_col, to_row, to_col, board):
            if abs(to_row - from_row) == abs(to_col - from_col):
                return self.clear_path(from_row, from_col, to_row, to_col, board)
        return False
