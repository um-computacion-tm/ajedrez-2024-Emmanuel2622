from board import *
from exceptions import *

class Chess:
    """
    Clase principal para gestionar un juego de ajedrez.
    """

    def __init__(self):
        """
        Inicializa el tablero de ajedrez y establece las configuraciones iniciales del juego.
        """
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__game_over__ = False
        self.__white_pieces__ = 0
        self.__black_pieces__ = 0
        self.__white_agrees__ = False
        self.__black_agrees__ = False

    def request_draw(self):
        """
        Permite a los jugadores solicitar un empate.

        Si ambos jugadores están de acuerdo en solicitar el empate,
        la partida se termina en tablas.

        Returns:
            str: Mensaje indicando si la partida ha terminado en empate o si se espera el acuerdo del otro jugador.
        """
        if self.__turn__ == "WHITE":
            self.__white_agrees__ = True
            print("Jugador blanco está de acuerdo en terminar la partida.")
        else:
            self.__black_agrees__ = True
            print("Jugador negro está de acuerdo en terminar la partida.")

        if self.__white_agrees__ and self.__black_agrees__:
            self.__game_over__ = True
            return "La partida ha terminado en empate."
        else:
            self.change_turn()
            return "Esperando a que ambos jugadores estén de acuerdo."

    def move(self, from_row, from_col, to_row, to_col):
        """
        Realiza un movimiento en el tablero de ajedrez.

        Valida si el movimiento es legal y cambia el turno del jugador si es válido.
        Si el movimiento no es válido, se captura una excepción y se devuelve un mensaje de error.

        Args:
            from_row (int): Fila inicial de la pieza.
            from_col (int): Columna inicial de la pieza.
            to_row (int): Fila destino de la pieza.
            to_col (int): Columna destino de la pieza.

        Returns:
            str: Mensaje de error si el movimiento no es válido. Si es válido, devuelve None.
        """
        try:
            if not all(isinstance(x, int) for x in [from_row, from_col, to_row, to_col]):
                raise ValueError("Valor no Numérico")
            if from_row < 0 or from_row > 7 or from_col < 0 or from_col > 7 or to_row < 0 or to_row > 7 or to_col < 0 or to_col > 7:
                raise OutOfBoard

            piece = self.__board__.get_piece(from_row, from_col)
            if piece is None:
                raise EmptyPosition
            if piece.__color__ != self.__turn__:
                raise InvalidTurn

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
        Verifica si el juego ha terminado al perder todas las piezas de un jugador.

        Cuenta las piezas de cada jugador y determina si alguno ha perdido todas.
        Si es así, devuelve True y declara un ganador.

        Returns:
            bool: True si el juego ha terminado, False en caso contrario.
        """
        self.__white_pieces__ = 0
        self.__black_pieces__ = 0

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
        Devuelve el turno actual del jugador.

        Returns:
            str: El color del jugador actual que tiene el turno ("WHITE" o "BLACK").
        """
        return self.__turn__

    def show_board(self):
        """
        Muestra el estado actual del tablero.

        Returns:
            str: Representación en cadena del tablero de ajedrez.
        """
        return str(self.__board__)

    def change_turn(self):
        """
        Cambia el turno del jugador actual.

        Alterna el turno entre "WHITE" y "BLACK".

        Returns:
            str: El nuevo turno después del cambio.
        """
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
        return self.__turn__
