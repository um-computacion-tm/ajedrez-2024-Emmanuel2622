from pieces import Piece

class Rook(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
                return "♖"
        else:
             return "♜"
     
    def type_move(self, from_row, from_col, to_row, to_col, board):

        #Movimiento Horizontal
        if from_row == to_row:
            #Verificamos la direccion del movimiento
            if to_col > from_col:
                step = 1
            else:
                step = -1
            
            #Verifica que no haya piezas en el camino
            for col in range(from_col + step, to_col, step):
                if board.get_piece(from_row, col) is not None:
                    return False
            
            #Verifica que en el destino no haya piezas y si hay que sean de otro color
            if board.get_piece(to_row, to_col) is None or board.get_piece(to_row, to_col).__color__ != self.__color__: 
                return True

        return False
    

    def move(self, from_row, from_col, to_row, to_col, board):
        if self.type_move(from_row, from_col, to_row, to_col, board):
            board.__positions__[to_row][to_col] = board.__positions__[from_row][from_col]
            board.__positions__[from_row][from_col] = None
            return True
        else:
            return "Error en el movimiento"