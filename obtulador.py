import math, time, os
from PIL import Image # Necesitas: pip install pillow

class Incinerador:
    def __init__(self, w=100, h=50):
        self.w, self.h = w, h
        self.grid = [[0.0 for _ in range(h)] for _ in range(w)]

    def cargar_mapa(self, path):
        img = Image.open(path).convert('L').resize((self.w, self.h))
        for x in range(self.w):
            for y in range(self.h):
                # La luminosidad se convierte en energía inicial
                self.grid[x][y] = img.getpixel((x, y)) / 25.5 

    def conveccion_y_entropia(self):
        new_grid = [[0.0 for _ in range(self.h)] for _ in range(self.w)]
        for x in range(1, self.w - 1):
            for y in range(1, self.h - 1):
                # Difusión (Convección simplificada)
                avg = (self.grid[x+1][y] + self.grid[x-1][y] + 
                       self.grid[x][y+1] + self.grid[x][y-1]) / 4.0
                new_grid[x][y] = (self.grid[x][y] * 0.8) + (avg * 0.2)
                # Entropía (enfriamiento constante)
                new_grid[x][y] = max(0.0, new_grid[x][y] - 0.1)
        self.grid = new_grid

    def render(self):
        output = "\033[H"
        for y in range(self.h):
            for x in range(self.w):
                v = self.grid[x][y]
                # Shader manual 24-bit
                r = int(min(255, v * 25))
                g = int(min(255, v * 15))
                b = int(min(255, v * 5))
                output += f"\033[38;2;{r};{g};{b}m█"
            output += "\n"
        print(output)

# Ejecución
i = Incinerador(100, 50)
# Asegúrate de tener una imagen 'input.bmp' en la misma carpeta
i.cargar_mapa('pixel-mario1.gif') 

while True:
    i.conveccion_y_entropia()
    i.render()
    time.sleep(0.03)