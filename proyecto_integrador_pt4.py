import os
import time
from typing import List, Tuple

def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def mostrar_laberinto(laberinto: List[List[str]]):
    for fila in laberinto:
        print(''.join(fila))
    print()

def main_loop(laberinto: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]):
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        limpiar_pantalla()
        laberinto[px][py] = 'P'
        mostrar_laberinto(laberinto)

        # Leer del teclado las teclas de flechas
        movimiento = input("Ingresa la dirección (W/A/S/D): ").upper()

        # Verificar si la posición tentativa es válida
        nueva_px, nueva_py = px, py
        if movimiento == 'W' and px - 1 >= 0 and laberinto[px - 1][py] != '#':
            nueva_px -= 1
        elif movimiento == 'A' and py - 1 >= 0 and laberinto[px][py - 1] != '#':
            nueva_py -= 1
        elif movimiento == 'S' and px + 1 < len(laberinto) and laberinto[px + 1][py] != '#':
            nueva_px += 1
        elif movimiento == 'D' and py + 1 < len(laberinto[0]) and laberinto[px][py + 1] != '#':
            nueva_py += 1

        # Actualizar posición y restaurar la anterior
        laberinto[px][py] = '.'
        px, py = nueva_px, nueva_py

def convertir_mapa(mapa: str) -> List[List[str]]:
    # Separar por filas y convertir a lista de caracteres
    return [list(fila) for fila in mapa.split("\n")]

if __name__ == "__main__":
    laberinto_str = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

    laberinto = convertir_mapa(laberinto_str)
    posicion_inicial = (0, 0)
    posicion_final = (len(laberinto) - 1, len(laberinto[0]) - 1)

    main_loop(laberinto, posicion_inicial, posicion_final)
