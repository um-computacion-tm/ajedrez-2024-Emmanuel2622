# Changelog

## [0.0.6] - 22-08-2024

### Added

- Se creo la funcion __"move"__ que toma el valor que retorna por la funcion __"type_move"__, en caso de ser __"True"__ mueve el peon a la poscion indicada.

- Se creo la funcion __"type_move"__ la cual valida si el movimiento es posible, luego se incorporo el primer movimiento de la pieza Pawn "Salto simple hacia adelate".
___
## [0.0.5] - 21-08-2024

### Added

- Se agregaro la funcion __"str"__ a todas las piezas del ajedrez y se colocaron sus respectivas figuras.

- Se crearon las clases de excepciones dentro del archivo `exceptions.py`

- Archivo `exceptions.py` creado.

### Removed

- Se borro el archivo `tablero.py`

___
## [0.0.4] - 20-08-2024

### Changed

- Se modifico el nombre del archivo `main.py` por `cli.py` 

### Added

- Se creo la funcion __"show_board"__ dentro de la clase __Chess__.

- Se creo la clase __knight__.
- Se creo la clase __king__.
- Se creo la clase __queen__.
- Se creo la clase __bishop__.

- Dentro de la clase __Board__, Se agregaron las posiciones de las piezas faltantes y se creo la funcion __"str"__ que imprime el tablero con sus piezas.

- Se agrgo la funcion __"str"__ a la clase __Rook__ que devuelve el color de la pieza.

- Archivo `queen.py` creado.
- Archivo `king.py` creado.
- Archivo `knight.py` creado.
- Archivo `bishop.py` creado.

### Removed

- Se elimino las validaciones de parametros de los inputs de la funcion __"play"__ del archivo `cli.py`.


___
## [0.0.3] - 17-08-2024

### Changed

- Se modifco las validacion de parametros de las entradas de la funcion __"move"__ del archivo `chess.py`

### Added 

- Se agregaron las validacion de parametros de entrada que faltaban de la funcion __"move"__ (__to_row__, __to_col__) del archivo `chess.py`.

___
## [0.0.2] - 16-08-2024

### Changed

- En el archivo `Chess.py` se modifico la forma de llamar la clase __Board__ en la funcion __"init"__ de la clase __Chess__, y los "string" que devuelven los __return__ de las validacion de parametros de las entradas de la funcion __"move"__ 

### Added

- Se creo la funcion __"turn"__ en la clase __Chess__ del archivo `chess.py`

- Se creo la clase __Board__ en el archivo `board.py`, tambien se creo las funciones __"init"__ y __"get_piece"__, se agrego en la funcion __"init"__ un bucle para la creacion del tablero y agregar las piezas __Rook__ en sus posiciones iniciales.

- Se creo la clase __Pawn__ en el archivo `pawn.py`.

- Se creo la clase __Pieces__ en el archivo `pieces.py`.

- Se creo la clase __Rook__ en el archivo `rook.py`.

- Se crearon las funciones __"main"__ y __"play"__, Se agregaron los parametros de que los valores ingresados en los inputs (__from_row__, __from_col__, __to_row__, __to_col__) de la funcion __"play"__ del archivo `main.py` sean mayores a 0 y menores a 7.

- Archivo `rook.py` creado.
- Archivo `pieces.py` creado.
- Archivo `tablero.py` creado.
- Archivo `pawn.py` creado.
- Archivo `main.py` creado.
- Archivo `Dockerfile` creado.

___
## [0.0.1] - 15-08-2024

### Added

- Se creo la clase __Chess__ y se le agrego las funciones __"move"__, __"init"__ y "__change_turn__", y se agregaron parametros para las entradas que espera la funcion __"move"__, en el archivo `chess.py`

- Archivo `CHANGELOG.md` creado.
- Archivo `Readme.md` creado.
- Archivo `.coveragerc` creado.
- Archivo `.gitignore` creado.
- Archivo `.codeclimate.yml` creado.
- Carpeta `.circle` creada.
- Archivo `.circle/.config.yml` creado.
- Archivo `chess.py` creado.
- Archivo `test_chess.py` creado.
- Archivo `Requirements.txt` creado.

