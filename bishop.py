from pieces import Piece

class Bishop(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
                return "♗"
        else:
             return "♝"
        
    def type_move(self, from_row, from_col, to_row, to_col, board):
        if abs(to_row - from_row) == abs(to_col - from_col):
            if to_row > from_row:
                row_step = 1
            else:
                row_step = -1
            if to_col > from_col:
                col_step = 1
            else:
                col_step = -1
            
            # Verifica que no haya piezas en el camino
            row = from_row + row_step
            col = from_col + col_step
            while row != to_row and col != to_col:
                if board.get_piece(row, col) is not None:
                    return False
                row += row_step
                col += col_step
                
            # Verifica si hay una pieza en el destino y si es de otro color
            if board.get_piece(to_row, to_col) is not None and board.get_piece(to_row, to_col).__color__ == self.__color__:
                return False

            return True    
        return False
