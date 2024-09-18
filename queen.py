from pieces import Piece

class Queen(Piece):
    white_str = "♕"
    black_str = "♛"
        
    def type_move(self, from_row, from_col, to_row, to_col, board):
        if self.color_igual(from_row, from_col,to_row, to_col, board):
            
            #Verificamos la direccion del movimiento
            if to_row > from_row:
                row_step = 1
            else:
                row_step = -1
            if to_col > from_col:
                col_step = 1
            else:
                col_step = -1

            if from_row == to_row:
                    #Verifica que no haya piezas en el la fila
                    for col in range(from_col + col_step, to_col, col_step):
                        if board.get_piece(from_row, col) is not None:
                            return False

            #Movimiento Vertical
            elif to_col == from_col:
                #Verifica que no haya piezas en el la columna
                for row in range(from_row + row_step, to_row, row_step):
                    if board.get_piece(row, from_col) is not None:
                        return False
                    
            if abs(to_row - from_row) == abs(to_col - from_col):
                print("paso 1")
                row = from_row + row_step
                col = from_col + col_step
                while row != to_row and col != to_col:
                        print("paso 2")
                        if board.get_piece(row, col) is not None:
                            print("paso 3")
                            return False
                        row += row_step
                        col += col_step
            return True
        
            