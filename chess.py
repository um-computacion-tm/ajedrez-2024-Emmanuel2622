from board import *
from exceptions import *

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"


    def move(self, from_row, from_col, to_row, to_col,):
        try:
            if not all(isinstance(x, int) for x in [from_row, from_col, to_row, to_col]):
                raise ValueError("Valor no Numerico")
            if from_row < 0 or from_row > 7:
                raise OutOfBoard
            if from_col < 0 or from_col > 7:
                raise OutOfBoard
            if to_row < 0 or to_row > 7:
                raise OutOfBoard
            if to_col < 0 or to_col > 7:
                raise OutOfBoard
            
            piece = self.__board__.get_piece(from_row, from_col)
            if piece is None:
                raise EmptyPosition
            if piece.__color__ != self.__turn__:
                raise InvalidTurn

            print(f"Piece at from position: {piece}")
            
            if piece.move(from_row, from_col, to_row, to_col, self.__board__) != "Error en el movimiento":
                self.change_turn()    
            else:
                raise InvalidMove
            
            
        except InvalidMove as e:
            return f"error: {e}"

        except EmptyPosition as e:
            return f"error: {e}"

        except OutOfBoard as e:
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