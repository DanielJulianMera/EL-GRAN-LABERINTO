import os
import random
from typing import List, Tuple

class Juego:
    def __init__(self, laberinto: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]):
        self.laberinto = laberinto
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def limpiar_pantalla(self):
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def mostrar_laberinto(self):
        for fila in self.laberinto:
            print(''.join(fila))
        print()

    def main_loop(self):
        px, py = self.posicion_inicial

        while (px, py) != self.posicion_final:
            self.limpiar_pantalla()
            self.laberinto[px][py] = 'P'
            self.mostrar_laberinto()

            movimiento = input("Ingresa la dirección (W/A/S/D): ").upper()

            nueva_px, nueva_py = px, py
            if movimiento == 'W' and px - 1 >= 0 and self.laberinto[px - 1][py] != '#':
                nueva_px -= 1
            elif movimiento == 'A' and py - 1 >= 0 and self.laberinto[px][py - 1] != '#':
                nueva_py -= 1
            elif movimiento == 'S' and px + 1 < len(self.laberinto) and self.laberinto[px + 1][py] != '#':
                nueva_px += 1
            elif movimiento == 'D' and py + 1 < len(self.laberinto[0]) and self.laberinto[px][py + 1] != '#':
                nueva_py += 1

            self.laberinto[px][py] = '.'
            px, py = nueva_px, nueva_py


class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas: str):
        super().__init__([], (0, 0), (0, 0))
        self.path_a_mapas = path_a_mapas
        self.cargar_mapa_aleatorio()

    def cargar_mapa_aleatorio(self):
        archivos = os.listdir(self.path_a_mapas)
        nombre_archivo = random.choice(archivos)
        path_completo = os.path.join(self.path_a_mapas, nombre_archivo)
        datos_mapa = self.leer_mapa_desde_archivo(path_completo)
        self.laberinto, self.posicion_inicial, self.posicion_final = datos_mapa

    def leer_mapa_desde_archivo(self, archivo: str) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
        with open(archivo, 'r') as file:
            lineas = file.readlines()
            # Tomamos la primera línea y dividimos en cuatro valores
            dimensiones = tuple(map(int, lineas[0].split()))
            filas, columnas = dimensiones[2], dimensiones[3]  # Tomamos las últimas dos dimensiones
            laberinto = [list(linea.strip()) for linea in lineas[1:filas + 1]]
            inicio, fin = lineas[0].split()[0:2], lineas[0].split()[2:4]
            posicion_inicial = tuple(map(int, inicio))
            posicion_final = tuple(map(int, fin))
        return laberinto, posicion_inicial, posicion_final


if __name__ == "__main__":
    juego = JuegoArchivo("path:/carpeta")
    juego.main_loop()