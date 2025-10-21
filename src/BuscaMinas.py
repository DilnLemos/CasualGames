import pygame
import random
class BuscaMinas:


    def __init__(self, alto, ancho, num_minas):
        self.alto = alto
        self.ancho = ancho
        self.num_minas = num_minas
        self.tablero = self.crear_tablero()
        self.juego_activo = True

    def crear_tablero(self):
        tablero = [[0 for _ in range(self.ancho)] for _ in range(self.alto)]
        minas = self.minas(tablero, self.num_minas)
        tablero_oculto = [['X' for _ in range(self.ancho)] for _ in range(self.alto)]

        print(f"mapa creado con {minas} minas")
        print(tablero_oculto)
        return tablero_oculto

    def minas(self, tablero, num_minas):
        minas_colocadas = 0
        while minas_colocadas < num_minas:
            fila = random.randint(0, self.alto - 1)
            columna = random.randint(0, self.ancho - 1)
            if tablero[fila][columna] != 'M':
                tablero[fila][columna] = 'M'
                minas_colocadas += 1
        return minas_colocadas
    
    