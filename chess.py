from board import *

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"


    def move(self, from_row, from_col, to_row, to_col,):
        try:
            if not all(isinstance(x, int) for x in [from_row, from_col, to_row, to_col]):
                raise ValueError("no se ingreso un valor numerico")
            if from_row < 0 or from_row > 7:
                return "Error value from_row, out range"
            if from_col < 0 or from_col > 7:
                return "Error value from_col, out range"
            if to_row < 0 or to_row > 7:
                return "Error value to_row, out range"
            if to_col < 0 or to_col > 7:
                return "Error value to_col, out range"
            else:
                piece = self.__board__.get_piece(from_row, from_col)
                self.change_turn()
                return "pass"
            
        except  ValueError as e:
            return(f"error: {e}")
    
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