from chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        #print(chess.show_board())
        print("turn: ", chess.turn)
        print("Ingrese valores Mayores a 0 y menores a 7 para las posiciones")
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))
        
        if from_row < 0 or from_row > 7:
            return "El valor from row debe ser mayor a 0 y menor a 7, vuelva a intentar"
        elif from_col < 0 or from_col > 7:
            return "El valor from col debe ser mayor a 0 y menor a 7, vuelva a intentar"
        elif to_row < 0 or to_row > 7:
            return "El valor to row debe ser mayor a 0 y menor a 7, vuelva a intentar"
        elif to_col < 0 or to_col > 7:
            return "El valor to col debe ser mayor a 0 y menor a 7, vuelva a intentar"
        else:
            chess.move(
                from_row,
                from_col,
                to_row,
                to_col,
            )
            return "pass"
        
    except Exception as e:
        return "error"

if __name__ == '__main__':
    main()
