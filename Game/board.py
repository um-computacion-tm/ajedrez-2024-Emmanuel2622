from Game.rook import Rook
from Game.pawn import Pawn
from Game.knight import Knight
from Game.bishop import Bishop
from Game.queen import Queen
from Game.king import King

class Board:
    def __init__(self):
        self.__positions__ = []

        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        #agregar mas piezas

        # Posicion de Rook
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][7] = Rook("WHITE")
        self.__positions__[7][0] = Rook("WHITE")

        # Posicion de Pawn
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")
            self.__positions__[6][i] = Pawn("WHITE")

        #Posicion de Knight
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[7][6] = Knight("WHITE")
        self.__positions__[7][1] = Knight("WHITE")        

        #Posicion de Bishop
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[7][5] = Bishop("WHITE")
        self.__positions__[7][2] = Bishop("WHITE")

        #Posicion de Queen
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

        #Posicion de King
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
        

    def get_piece(self, row, col):
        return self.__positions__[row][col]