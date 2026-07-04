import tkinter as tk
import math
import random
import time

class ParticulaMasa:
    def __init__(self, cx, cy):
        self.cx, self.cy = cx, cy
        self.angle = random.uniform(0, 2 * math.pi)
        self.dist = random.uniform(100, 200)
        self.masa = random.uniform(0.5, 2.0)  # El "peso" que les da carácter
        self.velocidad = 0.02 * self.masa    # Los pesados se mueven lento

    def actualizar(self, t):
        self.angle += self.velocidad
        # La oscilación individual crea el efecto de "inercia"
        radio = 150 + 20 * math.sin(t * self.masa) 
        return (self.cx + radio * math.cos(self.angle), 
                self.cy + radio * math.sin(self.angle))

class SistemaComplejo:
    def __init__(self, canvas):
        self.canvas = canvas
        # 30 nodos: un enjambre de partículas con "voluntad" propia
        self.nodos = [ParticulaMasa(300, 200) for _ in range(30)]

    def dibujar(self):
        self.canvas.delete("all")
        t = time.perf_counter()
        
        # Dibujamos las conexiones para ver la estructura de red
        for i, nodo in enumerate(self.nodos):
            x, y = nodo.actualizar(t)
            next_nodo = self.nodos[(i + 1) % len(self.nodos)]
            nx, ny = next_nodo.actualizar(t)
            
            # La línea que une la masa (el "hilo" de la realidad)
            self.canvas.create_line(x, y, nx, ny, fill="#408000")
            # El nodo (la partícula elemental)
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="#aaff00")

# --- CONTROLADOR DE MANIFESTACIÓN ---
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()
sistema = SistemaComplejo(canvas)

def loop():
    sistema.dibujar()
    root.after(20, loop)

loop()
root.mainloop()