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

### Modo Juego Desplegado con Docker
Para ejecutar el juego en un entorno Dockerizado, sigue estos pasos:
   
1. Construir la imagen de Docker:
   ```bash
   docker build -t ajedrez:latest .
   ```

2. Ejecutar el contenedor:
   ```bash
   docker run -it ajedrez:latest
   ```
Esto iniciará el juego de ajedrez en un contenedor de Docker, permitiéndote jugar desde la terminal.

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

### Modo Testing
Para ejecutar las pruebas unitarias del proyecto, sigue estos pasos:

1. Asegúrate de tener Docker instalado y ejecutándose.
2. Construir la imagen de Docker para pruebas (puedes tener un Dockerfile específico para pruebas si es necesario):
   ```bash
      docker build -t ajedrez:test -f Dockerfile.test .
   ```
3. Ejecutar el contenedor de pruebas:
   ```bash
   docker run ajedrez:test
   ```
Esto ejecutará las pruebas y generará un informe de cobertura si has configurado `coverage` en tu `Dockerfile` de pruebas.

## 🧪 Pruebas

Para ejecutar las pruebas unitarias sin Docker:
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