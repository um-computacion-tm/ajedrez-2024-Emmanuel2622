from pieces import Piece

class King(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
                return "♔"
        else:
             return "♚"
        
    def type_move(self, from_row, from_col, to_row, to_col, board):
        if abs(from_row - to_row) == 1 or (from_col - to_col) == 1 and board.get_piece(to_row, to_col).__color__ != self.__color__:
            return True
        
            