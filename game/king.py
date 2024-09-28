from game.pieces import Piece

class King(Piece):
    white_str = "♔"
    black_str = "♚"

    def __init__(self, color):
        super().__init__(color)
        self.__horizontal__ = True
        self.__vertical__ = True
        self.__diagonal__ = True

    def type_move(self, from_row, from_col, to_row, to_col, board):
        if self.is_same_color(from_row, from_col, to_row, to_col, board):
            return False

        if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1:
            return True

        return False