import signal
import sys
from chess import Chess
from exceptions import InvalidMove

def signal_handler(sig, frame, chess):
    """
    Maneja la señal SIGINT (Ctrl + C) solicitando un empate en el juego de ajedrez.

    Al detectar Ctrl + C, esta función pide el empate a ambos jugadores
    y termina el juego si ambos están de acuerdo.

    Args:
        sig (int): El número de la señal recibida.
        frame (frame object): El frame actual en la pila de llamadas (stack frame).
        chess (Chess): La instancia del juego de ajedrez.
    """
    print("\nCtrl + C detectado. Solicitando empate...")
    result = chess.request_draw()
    print(result)
    if chess.__game_over__:
        sys.exit(0)

def main():
    """
    Función principal que inicia el juego de ajedrez y gestiona el ciclo del juego.

    Esta función configura el manejador de señales para SIGINT y
    ejecuta el ciclo principal del juego hasta que termine.
    """
    chess = Chess()

    # Asocia el manejador de la señal SIGINT (Ctrl + C)
    signal.signal(signal.SIGINT, lambda sig, frame: signal_handler(sig, frame, chess))

    while not chess.__game_over__:
        play(chess)

def play(chess):
    """
    Gestiona una ronda de movimientos en el juego de ajedrez.

    Esta función imprime el tablero actual, indica el turno del jugador,
    solicita al jugador que ingrese las coordenadas para mover una pieza,
    y maneja cualquier error que ocurra, como movimientos inválidos.

    Args:
        chess (Chess): Instancia del juego de ajedrez que se está jugando.

    Exceptions:
        InvalidMove: Se lanza cuando el movimiento ingresado es inválido.
        Exception: Se maneja cualquier otro error inesperado.
    """
    try:
        # Imprime el tablero, el turno del jugador y las instrucciones.
        print(chess.show_board())
        print("Turno de:", chess.turn)
        print("Ingrese valores mayores a 0 y menores a 7 para las posiciones")

        # Asigna los valores ingresados en los inputs a las variables correspondientes.
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))

        chess.move(from_row, from_col, to_row, to_col)

    except InvalidMove:
        print("Movimiento inválido")
    except Exception as e:
        print("error:", e)

if __name__ == '__main__':
    """
    Punto de entrada del programa.

    Ejecuta la función `main()` para iniciar el ciclo principal del juego.
    """
    main()
