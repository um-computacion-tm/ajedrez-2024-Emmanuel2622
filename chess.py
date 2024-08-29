from board import *
from exceptions import *

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"


    def move(self, from_row, from_col, to_row, to_col,):
        try:
            if not all(isinstance(x, int) for x in [from_row, from_col, to_row, to_col]):
                raise ValueError("no se ingreso un valor numerico")
            if from_row < 0 or from_row > 7:
                raise ValueError("value from_row, fuera rango")
            if from_col < 0 or from_col > 7:
                raise ValueError("value from_col, fuera rango")
            if to_row < 0 or to_row > 7:
                raise ValueError("value to_row, fuera rango")
            if to_col < 0 or to_col > 7:
                raise ValueError("value to_col, fuera rango")
            
            piece = self.__board__.get_piece(from_row, from_col)
            if piece is None:
                 raise InvalidMovePiece("No hay pieza en la posición de origen")
            if piece.__color__ != self.__turn__:
                raise InvalidMovePawn ("Pieza del turno incorrecto")

            print(f"Piece at from position: {piece}")
            if isinstance(piece, Pawn):
                if piece.move(from_row, from_col, to_row, to_col, self.__board__) != "Error en el movimiento":
                    self.change_turn()
                    return "Movimiento exitoso"
                else:
                    raise InvalidMovePawn("Movimiento inválido para el peón")

        except InvalidMovePawn as e:
            return f"error: {e}"

        except InvalidMovePiece as e:
            return f"error: {e}"

        except ValueError as e:
            return f"error: {e}"

    
    @property        
    def turn(self):
        return self.__turn__
    
    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
            return self.__turn__
        else:
            self.__turn__ = "WHITE"
            return self.__turn__