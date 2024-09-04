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

            #Verifica que no haya piezas en el la fila
            for col in range(from_col + col_step, to_col, col_step):
                for row in range(from_row + row_step, to_row, row_step):
                    if board.get_piece(row, col) is not None:
                        return False
                    
            #Verifica que en el destino no haya piezas y si hay que sean de otro color
            if board.get_piece(to_row, to_col) is None or board.get_piece(to_row, to_col).__color__ != self.__color__: 
                return True
            
        return False
