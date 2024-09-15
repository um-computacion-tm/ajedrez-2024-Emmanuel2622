from pieces import Piece

class King(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
                return "♔"
        else:
             return "♚"   

    #Movimiento Vertical y Horizontal
    def type_move(self, from_row, from_col, to_row, to_col, board):
        
        if self.color_igual(from_row, from_col, to_row, to_col, board):
            if abs(from_row - to_row) == 1 or (from_col - to_col) == 1:
                return True
        return False