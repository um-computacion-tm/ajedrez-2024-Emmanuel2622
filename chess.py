from board import *

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"


    def move(self, from_row, from_col, to_row, to_col,):
        try:
            if from_row < 0 or from_row > 7:
                return "error value"
            elif from_col < 0 or from_col > 7:
                return "error value"
            else:
                return "pass"
            
        except  ValueError as e:
            print(f"error: {e}")
        
        piece = self.__board__.get_piece(from_row, from_col)
        self.change_turn()
    
    @property        
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"