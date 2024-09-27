from Game.pieces import Piece

class Pawn(Piece):        
    def __init__(self, color):
        super().__init__(color)
        self._first_move = True
    
    white_str = "♙"
    black_str = "♟"
    
    def type_move(self, from_row, from_col, to_row, to_col, board):
        direction = -1 if self.__color__ == "WHITE" else 1

        # Movimiento simple hacia adelante
        if from_col == to_col and to_row == from_row + direction:
            if board.get_piece(to_row, to_col) is None:
                self._first_move = False
                return True

        # Movimiento doble hacia adelante
        if from_col == to_col and to_row == from_row + 2 * direction and self._first_move:
            if board.get_piece(to_row, to_col) is None and board.get_piece(from_row + direction, from_col) is None:
                self._first_move = False
                return True

        # Ataque
        if abs(from_col - to_col) == 1 and to_row == from_row + direction:
            target_piece = board.get_piece(to_row, to_col)
            if target_piece is not None and target_piece.__color__ != self.__color__:
                self._first_move = False
                return True

        return False
