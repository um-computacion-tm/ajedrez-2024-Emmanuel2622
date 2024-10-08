from chess import Chess
from exceptions import InvalidMove

def main():
    """
    Función principal que inicia el juego de ajedrez.

    Esta función crea una instancia de la clase `Chess` y entra en un ciclo infinito
    llamando a la función `play()` en cada iteración para gestionar el flujo del juego.
    """
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    """
    Gestiona una ronda de movimientos en el juego de ajedrez.

    Esta función imprime el tablero de ajedrez actual, indica el turno del jugador,
    y solicita al jugador que ingrese las coordenadas para mover una pieza.
    Luego, intenta mover la pieza y maneja cualquier error que ocurra, como movimientos inválidos.

    Args:
        chess (Chess): Instancia del juego de ajedrez que se está jugando.

    Exceptions:
        InvalidMove: Se lanza cuando el movimiento ingresado es inválido.
        Exception: Se maneja cualquier otro error inesperado y lo imprime.
    """
    try:
        # Imprime el tablero, el turno del jugador y las condiciones de los inputs.
        print(chess.show_board())
        print("Turno de:", chess.turn)
        print("Ingrese valores mayores a 0 y menores a 7 para las posiciones")

        # Asigna los valores ingresados en los inputs a cada variable.
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))

        chess.move(from_row, from_col, to_row, to_col)

    except InvalidMove as e:
        print("Movimiento inválido")
    except Exception as e:
        print("error", e)

if __name__ == '__main__':
    """
    Punto de entrada del programa.

    Ejecuta la función `main()` para iniciar el ciclo principal del juego.
    """
    main()
