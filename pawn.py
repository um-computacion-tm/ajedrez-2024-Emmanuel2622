from pieces import Piece

class Pawn(Piece):        
    white_str = "♙"
    black_str = "♟"

    def __init__(self, color):
        """
        Inicializa un objeto de tipo Pawn (peón) con un color específico.

        Args:
            color (str): El color de la pieza, puede ser 'WHITE' o 'BLACK'.
        """
        super().__init__(color)
        self._first_move = True  # Indica si el peón ha realizado su primer movimiento

    def type_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento del peón es válido.

        Los peones se mueven hacia adelante y pueden avanzar una o dos casillas en su primer movimiento. 
        También pueden atacar piezas en diagonales.

        Args:
            from_row (int): Fila de origen del peón.
            from_col (int): Columna de origen del peón.
            to_row (int): Fila de destino del peón.
            to_col (int): Columna de destino del peón.
            board (Board): El tablero que contiene todas las piezas.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        direction = -1 if self.__color__ == "WHITE" else 1

        # Movimiento simple hacia adelante
        if from_col == to_col and to_row == from_row + direction:
            if board.get_piece(to_row, to_col) is None:  # Verifica que la casilla de destino esté vacía
                self._first_move = False  # Marca que el peón ya no es su primer movimiento
                return True

        # Movimiento doble hacia adelante
        if from_col == to_col and to_row == from_row + 2 * direction and self._first_move:
            if (board.get_piece(to_row, to_col) is None and
                board.get_piece(from_row + direction, from_col) is None):  # Verifica que ambas casillas estén vacías
                self._first_move = False  # Marca que el peón ha realizado su primer movimiento
                return True

        # Ataque
        if abs(from_col - to_col) == 1 and to_row == from_row + direction:
            target_piece = board.get_piece(to_row, to_col)
            if target_piece is not None and target_piece.__color__ != self.__color__:
                self._first_move = False  # Marca que el peón ha atacado
                return True

        return False
