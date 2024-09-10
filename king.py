from pieces import Piece

class King(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
                return "♔"
        else:
             return "♚"