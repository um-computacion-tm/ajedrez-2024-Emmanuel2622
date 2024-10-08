from pieces import Piece

class Queen(Piece):
    white_str = "♕"
    black_str = "♛"

    def __init__(self, color):
        """
        Inicializa un objeto de tipo Queen (reina) con un color específico.

        Args:
            color (str): El color de la pieza, puede ser 'WHITE' o 'BLACK'.
        """
        super().__init__(color)
        self.__horizontal__ = True
        self.__vertical__ = True
        self.__diagonal__ = True

    def type_move(self, from_row, from_col, to_row, to_col, board):
        """
        Verifica si el movimiento de la reina es válido.

        La reina se puede mover en línea recta horizontal, vertical o diagonal,
        siempre que no haya piezas que bloqueen su camino.

        Args:
            from_row (int): Fila de origen de la reina.
            from_col (int): Columna de origen de la reina.
            to_row (int): Fila de destino de la reina.
            to_col (int): Columna de destino de la reina.
            board (Board): El tablero que contiene todas las piezas.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        # Verifica si el movimiento no es hacia una casilla ocupada por una pieza del mismo color
        if self.is_same_color(from_row, from_col, to_row, to_col, board):
            return False
        
        # Verifica si hay un camino despejado para el movimiento
        return self.clear_path(from_row, from_col, to_row, to_col, board)
