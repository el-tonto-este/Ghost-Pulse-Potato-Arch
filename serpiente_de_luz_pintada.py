import math
import os
import time

class MotorEntropico:
    def __init__(self, ancho=40, alto=20):
        self.ancho = ancho
        self.alto = alto
        self.mapa = [[0.0 for _ in range(alto)] for _ in range(ancho)]
        self.t = 0.0

    def mover_boson(self):
        self.t += 0.2
        denom = 1 + math.sin(self.t)**2
        x = int((self.ancho / 2) + (self.ancho / 2.5) * math.cos(self.t) / denom)
        y = int((self.alto / 2) + (self.alto / 2.5) * math.sin(self.t) * math.cos(self.t) / denom)
        # Asegurar límites
        x, y = max(0, min(self.ancho-1, x)), max(0, min(self.alto-1, y))
        # Inyección de energía
        self.mapa[x][y] = min(10.0, self.mapa[x][y] + 5.0)
        return x, y

    def aplicar_entropia(self):
        for x in range(self.ancho):
            for y in range(self.alto):
                if self.mapa[x][y] > 0:
                    self.mapa[x][y] = max(0.0, self.mapa[x][y] - 0.5)

    def render(self):
        chars = " .:-=+*#%@" # Degradado de densidad
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.alto):
            fila = ""
            for x in range(self.ancho):
                intensidad = int(self.mapa[x][y] / 10 * (len(chars)-1))
                fila += chars[intensidad]
            print(fila)

# Bucle principal
motor = MotorEntropico()
try:
    while True:
        motor.mover_boson()
        motor.aplicar_entropia()
        motor.render()
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nSistema apagado. Bitácora cerrada.")