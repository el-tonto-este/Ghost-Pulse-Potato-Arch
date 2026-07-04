import tkinter as tk
import math
import random
import time
import colorsys # Importamos para generar colores espectrales

class ParticulaColor:
    def __init__(self, cx, cy, indice, total):
        self.cx, self.cy = cx, cy
        self.angle = random.uniform(0, 2 * math.pi)
        # La distancia varía para crear capas
        self.dist = random.uniform(100, 250)
        # La masa afecta a la frecuencia (peso individual)
        self.masa = random.uniform(0.6, 2.4) 
        self.velocidad = 0.02 * self.masa
        
        # Asignamos un color basado en su posición en el círculo (espectro)
        # colorsys.hsv_to_rgb(H, S, V) -> H va de 0.0 a 1.0 (tono)
        hue = indice / total
        rgb_norm = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        # Convertimos a formato hexadecimal (#RRGGBB)
        self.color = f'#{int(rgb_norm[0]*255):02x}{int(rgb_norm[1]*255):02x}{int(rgb_norm[2]*255):02x}'

    def actualizar(self, t):
        self.angle += self.velocidad
        radio = 150 + 40 * math.sin(t * self.masa) 
        return (self.cx + radio * math.cos(self.angle), 
                self.cy + radio * math.sin(self.angle),
                self.color)

class SistemaCromatico:
    def __init__(self, canvas):
        self.canvas = canvas
        num_nodos = 36 # Aumentamos nodos para más densidad de color
        self.nodos = [ParticulaColor(300, 200, i, num_nodos) for i in range(num_nodos)]

    def dibujar(self):
        self.canvas.delete("all")
        t = time.perf_counter()
        
        # Puntos de anclaje para las conexiones
        positions = []
        for nodo in self.nodos:
            positions.append(nodo.actualizar(t))

        # Dibujar conexiones (hilos de luz de colores)
        for i in range(len(positions)):
            x, y, color = positions[i]
            nx, ny, ncolor = positions[(i + 1) % len(positions)]
            
            # La línea es la media de los colores de los dos nodos
            # Tkinter no soporta gradientes en líneas, usamos un color intermedio
            # Esto es una aproximación simple de mezcla aditiva
            r1 = int(color[1:3], 16); g1 = int(color[3:5], 16); b1 = int(color[5:7], 16)
            r2 = int(ncolor[1:3], 16); g2 = int(ncolor[3:5], 16); b2 = int(ncolor[5:7], 16)
            mid_color = f'#{int((r1+r2)/2):02x}{int((g1+g2)/2):02x}{int((b1+b2)/2):02x}'

            self.canvas.create_line(x, y, nx, ny, fill=mid_color, width=1.5)
            
        # Dibujar partículas (los nodos elementales)
        for x, y, color in positions:
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=color, outline="#ffffff", width=0.5)

# --- CONTROLADOR DE MANIFESTACIÓN CROMÁTICA ---
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400, bg="#111111") # Fondo gris muy oscuro
canvas.pack()
sistema = SistemaCromatico(canvas)

def loop():
    sistema.dibujar()
    root.after(30, loop)

loop()
root.mainloop()