from pieces import Piece

class Pawn(Piece):        
    def __str__(self):
        if self.__color__ == "WHITE":
                return "♙"
        else:
             return "♟"

    def type_move(self, from_row, from_col, to_row, to_col, board):
        if self.__color__ == "WHITE":
            direction = -1
        else:
            direction = 1

        # Validacion movimiento simple hacia adelante
        if from_col == to_col and to_row == from_row + direction:
            #Verifica que no tenga ninguna pieza adelante
            if board.get_piece(to_row, to_col) is None:
                print("salto")
                return True

        # Validacion movimiento doble hacia adelante    
        if from_col == to_col and to_row == from_row + 2 * direction and self.__first_move__ == True:
            print("salto doble")
            if board.get_piece(to_row, to_col) is None:
                if (self.__color__ == "WHITE" and from_row == 6) or (self.__color__ == "BLACK" and from_row == 1):
                    #Verifica que no tenga ninguna pieza adelante
                    if board.get_piece(from_row + direction, from_col) is None:
                        return True
        # Ataque
        if abs(from_col - to_col) == 1 and to_row == from_row + direction:
            target_piece = board.get_piece(to_row, to_col)
            if target_piece is not None and target_piece.__color__ != self.__color__:
                print("Comio")
                return True
        return False
    
    def move(self, from_row, from_col, to_row, to_col, board):
        if self.type_move(from_row, from_col, to_row, to_col, board):
            board.__positions__[to_row][to_col] = board.__positions__[from_row][from_col]
            board.__positions__[from_row][from_col] = None
            self.__first_move__ = False
            return True
        else:
            return "Error en el movimiento"