# Changelog

## [0.2.8] - 27-9-2024

### Added

- Se creo el movimiento de las pieza __knight__.

___

## [0.2.7] - 26-9-2024

### Changed

- Se pasaron los __test__ a la carpeta `Test`, y se agregaron mas test en el archivo `test_rook.py` y `test_queen.py`.

- Se pasasron los archivos del Juego a la carpeta `Game` .

### Added

- Carpeta `Game` creada.

- Carpeta `Test` creada.
___

## [0.2.6] - 24-9-2024

### Added

- Se agregaron las variables __horizontal__, __vertical__, __diagonal__ a las piezas para validar sus tipos de movimientos.

### Fixed

- Se arreglo un error en la ejecucion del metodo __move__ en el archivo `chess.py`, ya que se llamaba dos veces al metodo y eso ocasionaba un error.

### Changed

- Se arreglo el test: __test_move_diagonal_good__. Del archivo `test_queen.py`.
___

## [0.2.5] - 23-9-2024

### Changed

- Se elimino la repeticion de codigo de las piezas y se pasaron los movimientos al archivo `pieces.py`.

___

## [0.2.4] - 21-9-2024

### Changed

- Se modifico el metodo de verificaicon del movimiento de la pieza en el archivo `chess.py`.

- Se agrego un test en el archivo `test_queen.py`, para cubrir el 100%.

___

## [0.2.3] - 19-9-2024

### Changed

- Se simplifico los test de las piezas para no repetir codigo.

___

## [0.2.2] - 18-9-2024

### Added

- Archivo `test_queen.py` creado con los test de la pieza __Queen__.

___

## [0.2.1] - 17-9-2024

### Added

- Se creo los movimientos del la pieza __Queen__.

### Changed

- Se modificaron las exceptions.

- Se movio al archivo `pieces.py` la asignacion de color de las piezas. 

- Se modifico la condicion del movimiento del la pieza __King__ para que pueda moverse en diagonal.

___

## [0.2.0] - 16-9-2024

### Added

- Archivo `test_king.py` creado mas los test para la pieza __King__.

___

## [0.1.9] - 15-9-2024

### Changed

- Se paso la verificacion que tenian las piezas para saber si el destino tenia una pieza y era del mimso color, al archivo `pieces.py`.

___

## [0.1.8] - 13-9-2024

### Added

- Se creo el movimiento de la pieza __king__. 

___

## [0.1.7] - 11-9-2024

### Changed

- Se movio la funcion __"move"__ al archivo `pieces.py`.

___

## [0.1.6] - 10-9-2024

### Changed

- En el archivo `bishop.py` se cambio la forma de verificar las casillas antes del movimiento.

- Se arreglo el test del archivo `board.py`.

### Added

- Se crearon los test para la pieza __bishop__. 

- Archivo `test_bishop.py` creado.

___

## [0.1.5] - 8-09-2024

### Fixed

- Se arreglo las posciones de la pieza Bishop y Knight.

## [0.1.4] - 3-09-2024

### Added

- En el arcvivo `bishop.py`, se creo la funcion __"move"__.
___

## [0.1.4] - 3-09-2024

### Added

- En el archivo `bishop.py`, Se creo la funcion __"type_move"__.

___

## [0.1.3] - 2-09-2024

### Fixed

- Se modifico en el archivo `board.py` las posiciones de las piezas, ya que habian piezas mal ubicadas y eso ocasionaba un error al querer moverlas.

## [0.1.2] - 30-08-2024

### Changed

- En el archivo `chess.py`, se realizo una simplificación de la lógica condicional eliminando la verificación de __"isinstance"__ para la clase Pawn antes de llamar al método move. Ahora se llama directamente a todos los tipos de piezas.

___

## [0.1.2] - 30-08-2024

### Fixed

- Se movio la variable "__first_move__" del archivo `pieces.py` al archivo `pawn.py` por un bug que ocasionaba.

### Added

- En el archivo `rook.py`, se creo el movimiento vertical de la torre del ajedrez.

- Se agregaron test en `test_rook.py`.

___

## [0.1.1] - 29-08-2024

### Added

- En el archivo `rook.py`, se creo el movimiento horizontal de la torre del ajedrez.

- Archivo `test_rook.py` creado.

___

## [0.1.0] - 28-08-2024

### Changed

- En el archivo `chess.py`, se modificaron los return de errores.

### Added

- En el archivo `pieces.py` se incorporo la variable "__first_move__"

- En el archivo `chess.py`, se agrego la funcion __isinstance__ y una comprobacion para verificar que el movimiento de la pieza sea __"True"__, en ese caso devuelve "__Movimiento exitoso__"

- En el archivo `test_chess.py` se agregaron mas test para comprobar el correcto funcionamiento del Ajedrez
___

## [0.0.9] - 25-08-2024

### Added

- En el archivo `pawn.py`, se creo el ataque del peon en diagonal, con las condiciones de que solo pueda comer si el salto es de una fila y una columna de diferencia.

- En el archivo `test_pawn.py` ,se agregaron los test para comprobar el correcto funcionamiento del ataque en diagonal. 

___

## [0.0.8] - 24-08-2024

### Added

- En el archivo `pawn.py`, se incorporo el segundo movimiento del peon, "Salto doble hacia adelante".

- En el archivo `pawn.py`, se creo la variable __"first_move"__ para verificar si es el primer movimiento del peon, en caso de ser _"True"_, el salto doble es valido.

- En el archivo `test_pawn.py`, se agregaron los test para comprobar el correcto funcionamiento del salto doble del peon.

___

## [0.0.7] - 23-08-2024

### Added

- En el archivo `pawn.py`, se creo la funcion __"move"__ que toma el valor que retorna por la funcion __"type_move"__, en caso de ser __"True"__ mueve el peon a la poscion indicada.

- En el archivo `pawn.py`, se creo la funcion __"type_move"__ la cual valida si el movimiento es posible, luego se incorporo el primer movimiento de la pieza Pawn "Salto simple hacia adelate".

- Archivo `test_pawn.py` creado.

___

## [0.0.6] - 21-08-2024

### Added

- Se agregaro la funcion __"str"__ a todas las piezas del ajedrez y se colocaron sus respectivas figuras.

- Se crearon las clases de excepciones dentro del archivo `exceptions.py`

- Archivo `exceptions.py` creado.

### Removed

- Se borro el archivo `tablero.py`

___

## [0.0.5] - 20-08-2024

### Changed

- Se modifico el nombre del archivo `main.py` por `cli.py` 

- Se modifico el nombre del archivo `test_main.py` por `test_cli.py`

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

## [0.0.4] - 19-08-2024

### Added

- Se crearon los test para las posiciones de las piezas en el tablero.

- Archivo `test_board.py` creado.

___

## [0.0.3] - 17-08-2024

### Changed

- Se modifco las validacion de parametros de las entradas de la funcion __"move"__ del archivo `chess.py`.

### Added 

- Se agregaron las validacion de parametros de entrada que faltaban de la funcion __"move"__ (__to_row__, __to_col__) del archivo `chess.py`.

___

## [0.0.2] - 16-08-2024

### Changed

- En el archivo `Chess.py` se modifico la forma de llamar la clase __Board__ en la funcion __"init"__ de la clase __Chess__, y los "string" que devuelven los __return__ de las validacion de parametros de las entradas de la funcion __"move"__.

### Added

- Se creo la funcion __"turn"__ en la clase __Chess__ del archivo `chess.py`.

- Se creo la clase __Board__ en el archivo `board.py`, tambien se creo las funciones __"init"__ que contiene un bucle para la creacion del tablero y agregar las piezas __Rook__ en sus posiciones iniciales, y la funcion __"get_piece"__ que devuelve la posicion del la pieza ingresada en los parametros.

- Se creo la clase __Pawn__ en el archivo `pawn.py`.

- Se creo la clase __Pieces__ en el archivo `pieces.py`.

- Se creo la clase __Rook__ en el archivo `rook.py`.

- Se crearon las funciones __"main"__ y __"play"__ y se agregaron las condiciones para que los valores ingresados en los inputs (__from_row__, __from_col__, __to_row__, __to_col__) de la funcion __"play"__ del archivo `main.py` sean mayores a 0 y menores a 7.

- Archivo `board.py` creado.
- Archivo `rook.py` creado.
- Archivo `pieces.py` creado.
- Archivo `tablero.py` creado.
- Archivo `pawn.py` creado.
- Archivo `main.py` creado.
- Archivo `test_main.py` creado.
- Archivo `Dockerfile` creado.

___

## [0.0.1] - 14-08-2024

### Added

- Se creo la clase __Chess__ y se le agrego las funciones __"move"__, __"init"__ y "__change_turn__", tambien se agregaron las condiciones para los parametros que espera la funcion __"move"__, en el archivo `chess.py`.

- Se crearon los test que evaluan las validacion de los parametros ingresados en la funcion __"move"__ `chess.py`.

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

