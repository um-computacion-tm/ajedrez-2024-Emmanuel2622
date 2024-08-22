from chess import Chess
from exceptions import InvalidMove

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        # Imprime el tablero, el turno del jugador y las condiciones de los inputs.
        print(chess.show_board())
        print("turn: ", chess.turn)
        print("Ingrese valores Mayores a 0 y menores a 7 para las posiciones")
        # Asigna los valores ingresados en los inputs en cada variable.
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col,
        )
        
    except InvalidMove as e:
        print("Movimiento invalido")
    except Exception as e:
        print("error", e)

if __name__ == '__main__':
    main()
