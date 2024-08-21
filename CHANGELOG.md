# Changelog

## [0.0.4] - 20-08-2024

### Removed

- Se elimino la comprobacion de los valores ingresados en los inputs de la funcion play.

## Added

- Se crearon las class knight, king, queen, bishop. Y se agrego en el archivo board.py sus posiciones.

- Se le agrego la funcion "__str__" a la class Rock, con una comprobacion del color de la posicion para asignarle el color a su figura. Tambien se le agrego la funcion "__str__" a la class Board

## [0.0.3] - 17-08-2024

### Changed

- Se modifico los return de las comprobaciones de las entradas que espera la funcion mov del archivo chess.py.

### Added 

- Se agrego las comprobaciones de que los valores igresados en (to_row, to_col) de la funcion mov del archivo chess.py sean mayores a 0 y menores a 7.

## [0.0.2] - 16-08-2024

### Changed

- Se modifico el str que devuelve el return de las lineas 12, 14

### Added

- Se agrego las comprobaciones de que los valores ingresados en los inputs (from_row, from_col, to_row, to_col) de la funcion play del archivo main.py sean mayores a 0 y menores a 7.

- Se agrego la funcion turn

- Se crearon los archivos rook.py, pieces.py, tablero.py, pawn.py

### Fixed

- En el archivo Chess.py se arreglo la forma de llamar a la clase board en la linea 5.


## [0.0.1] - 15-08-2024

### Added

- Se agrego las comprobaciones de que los valores ingresados en (from_row, from_col) de la funcion mov del archivo chess.py sean mayores a 0 y menores a 7.
