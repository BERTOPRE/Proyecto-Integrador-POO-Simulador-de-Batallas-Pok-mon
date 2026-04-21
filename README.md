# Proyecto Batallas Pokémon
## Michael Pérez


# Simulador de Batallas Pokémon con Python

Proyecto desarrollado en Python aplicando Programación Orientada a Objetos (POO).  
El sistema permite simular combates Pokémon en consola en dos modos de juego:

- Jugador vs Jugador
- Jugador vs Computadora

## Descripción

Este proyecto fue creado con fines de aprendizaje para practicar conceptos fundamentales de Python y POO, como:

- clases y objetos
- herencia
- encapsulamiento
- organización modular del código
- lógica de combate por turnos
- manejo de entradas del usuario

El jugador puede seleccionar un Pokémon desde un catálogo y participar en una batalla por turnos donde cada participante puede atacar, defenderse o descansar.

## Características

- Menú principal interactivo
- Catálogo de Pokémon disponibles
- Selección de Pokémon por jugador
- Modo Jugador vs Jugador
- Modo Jugador vs Computadora
- Sistema de combate por turnos
- Acciones disponibles:
  - atacar
  - defender
  - descansar
- Estados durante la batalla, como parálisis
- Determinación automática de quién inicia el combate
- Estructura modular para facilitar mantenimiento y ampliación

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos
- Consola / terminal

## Estructura del proyecto

```bash
Proyecto-Integrador-POO-Simulador-de-Batallas-Pok-mon/
│
├── main.py
├── datos/
│   ├── pokedex.py
│   ├── reglas_acciones.py
│   └── tipos_pokemon.py
│
├── modelos/
│   ├── jugador.py
│   ├── pokemon.py
│   ├── pokemon_agua.py
│   ├── pokemon_fuego.py
│   ├── pokemon_planta.py
│   ├── pokemon_electrico.py
│   └── pokemon_clases.py
│
├── servicios/
│   ├── acciones/
│   │   ├── ataque.py
│   │   ├── defensa.py
│   │   └── descanso.py
│   │
│   ├── combate/
│   │   ├── jugador_vs_jugador.py
│   │   └── jugador_vs_computadora.py
│   │
│   ├── estados/
│   │   ├── critico.py
│   │   └── debilitado.py
│   │
│   └── pokemon/
│       └── crear_pokemon.py
│
└── utilidades/
    ├── menu.py
    ├── menu_pokedex.py
    └── determinar_inicio_combate.py
