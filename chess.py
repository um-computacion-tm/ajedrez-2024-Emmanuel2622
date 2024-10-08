from board import *
from exceptions import *

class Chess:
    def __init__(self):
        """
        Inicializa el juego de ajedrez, creando un tablero, estableciendo el turno inicial 
        como "WHITE", y configurando las variables de control del juego.
        """
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__game_over__ = False
        self.__white_pieces__ = self.__black_pieces__ = 0

    def move(self, from_row, from_col, to_row, to_col):
        """
        Intenta realizar un movimiento en el tablero desde una posición de origen
        a una posición de destino. Valida los parámetros y el estado del juego antes 
        de realizar el movimiento.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            str: Un mensaje de error si ocurre un problema durante el movimiento, 
            o el turno si el movimiento es exitoso.
        """
        try:
            if self.__game_over__:
                return "La partida ha terminado."

            if not all(isinstance(x, int) for x in [from_row, from_col, to_row, to_col]):
                raise ValueError("Valor no Numerico")
            if from_row < 0 or from_row > 7 or from_col < 0 or from_col > 7 or to_row < 0 or to_row > 7 or to_col < 0 or to_col > 7:
                raise OutOfBoard

            piece = self.__board__.get_piece(from_row, from_col)
            if piece is None:
                raise EmptyPosition
            if piece.__color__ != self.__turn__:
                raise InvalidTurn

            print(f"Piece at from position: {piece}")

            if piece.move(from_row, from_col, to_row, to_col, self.__board__) != "Error en el movimiento":
                self.change_turn()    
                if self.check_game_over():
                    self.__game_over__ = True
                    print(f"El jugador {self.__turn__} ha ganado la partida.")
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

    def check_game_over(self):
        """
        Verifica si alguno de los jugadores ha perdido todas sus piezas. 
        Esto determinaría el final del juego.

        Returns:
            bool: True si el juego ha terminado, False en caso contrario.
        """
        for row in self.__board__.__positions__:
            for piece in row:
                if piece is not None:
                    if piece.__color__ == "WHITE":
                        self.__white_pieces__ += 1
                    elif piece.__color__ == "BLACK":
                        self.__black_pieces__ += 1

        if self.__white_pieces__ == 0:
            print("Las piezas blancas han sido eliminadas. ¡Ganan las negras!")
            return True
        elif self.__black_pieces__ == 0:
            print("Las piezas negras han sido eliminadas. ¡Ganan las blancas!")
            return True
        return False

    @property        
    def turn(self):
        """
        Obtiene el turno actual del juego.

        Returns:
            str: El color del jugador que tiene el turno ("WHITE" o "BLACK").
        """
        return self.__turn__

    def show_board(self):
        """
        Muestra el estado actual del tablero.

        Returns:
            str: Representación en cadena del tablero.
        """
        return str(self.__board__)

    def change_turn(self):
        """
        Cambia el turno del jugador actual.

        Returns:
            str: El nuevo turno del jugador.
        """
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
        return self.__turn__
