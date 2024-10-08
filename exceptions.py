class InvalidMove(Exception):
    message = "Movimiento de pieza Invalido"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    message = "No puede mover una pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"

class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"

