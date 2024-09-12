from pieces import Piece

class Rook(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
                return "♖"
        else:
             return "♜"
     
    def type_move(self, from_row, from_col, to_row, to_col, board):
        #Verificamos la direccion del movimiento
        if to_col > from_col or to_row > from_row:
            step = 1
        else:
            step = -1

        #Movimiento Horizontal
        if from_row == to_row:

            #Verifica que no haya piezas en el la fila
            for col in range(from_col + step, to_col, step):
                if board.get_piece(from_row, col) is not None:
                    return False
            
            #Verifica que en el destino no haya piezas y si hay que sean de otro color
            if board.get_piece(to_row, to_col) is None or board.get_piece(to_row, to_col).__color__ != self.__color__: 
                return True
        #Movimiento Vertical
        elif to_col == from_col:
            #Verifica que no haya piezas en el la columna
            for row in range(from_row + step, to_row, step):
                if board.get_piece(row, from_col) is not None:
                    return False
            
            #Verifica que en el destino no haya piezas y si hay que sean de otro color
            if board.get_piece(to_row,to_col) is None or board.get_piece(to_row, to_col).__color__ != self.__color__:
                return True

        return False
    