# Juego de Ajedrez - 2024
Este proyecto implementa un juego de ajedrez simple donde dos jugadores pueden competir entre sí. El juego gestiona el tablero de ajedrez, valida los movimientos y verifica si un jugador ha ganado o si ambos jugadores acuerdan un empate. El juego está construido en Python con un enfoque en un diseño orientado a objetos limpio.

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-Emmanuel2622/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-Emmanuel2622/tree/main)
[![Maintainability](https://api.codeclimate.com/v1/badges/68ee2052845e730b851a/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Emmanuel2622/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/68ee2052845e730b851a/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Emmanuel2622/test_coverage)

## 🛠️ Características
- **Visualización del Tablero de Ajedrez**: Representación visual del estado actual del juego en la terminal.
- **Validación de Movimientos**: Asegura que cada movimiento sea legal según las reglas del ajedrez.
- **Rotación de Turnos**: Alterna los turnos entre jugadores automáticamente.
- **Acuerdo de Empate**: Ambos jugadores pueden acordar un empate, lo que termina el juego.
- **Manejo de Señales**: Detecta `Ctrl + C` para una solicitud de empate.
  
## 🚀 Instalación
Para comenzar con el juego de ajedrez, sigue estas instrucciones:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/um-computacion-tm/ajedrez-2024-Emmanuel2622.git

2. Navega al directorio del proyecto:
   ```bash
   cd ajedrez-2024-Emmanuel2622
   ```
3. Instala las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
   ```
## 📦 Uso
Para jugar, simplemente ejecuta el archivo principal:
   ```bash
   python cli.py
   ```
El juego comenzará, mostrando el tablero de ajedrez y pidiéndote que ingreses las coordenadas para tus movimientos.

### Ejemplo de Movimiento:
Cuando sea tu turno, puedes mover una pieza proporcionando las coordenadas de origen y destino:
   ```bash
   Turno de: WHITE
   From row: 1
   From col: 0
   To row: 2
   To col: 0
   ```
Puedes salir del juego y solicitar un empate en cualquier momento presionando Ctrl + C.

## 🧪 Tests

Para ejecutar las pruebas unitarias del proyecto:
   ```bash
   coverage run -m unittest
   ```
Para generar un informe de cobertura:
```bash
   coverage report -m
   ```

## 🛡️ CI/CD & Quality

- CircleCI: Pruebas automatizadas e integración continua con CircleCI.
- Code Climate: Análisis de mantenibilidad del código y cobertura de pruebas.

## Autor

Carlos Emmanuel Denis

ce.denis@alumno.um.edu.ar