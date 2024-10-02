from pieces import Piece

class Knight(Piece):
    white_str = "♘"
    black_str = "♞"
    
    def type_move(self, from_row, from_col, to_row, to_col, board):
        """Verifica que el movimiento sea en forma de L y no haya pieza del mismo color en el destino."""
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            # Verificar que no haya una pieza del mismo color en la casilla de destino
            if not self.is_same_color(from_row, from_col, to_row, to_col, board):
                return True
        return False
