import tkinter as tk
import math
import time

class Manifestacion:
    def __init__(self, canvas):
        self.canvas = canvas
        self.num_nodos = 18
        self.centro = (300, 200)
        # Aquí guardamos la "esencia" del objeto, no su posición física
        self.fase_base = 0

    def dibujar(self):
        self.canvas.delete("all")
        t = time.time()
        cx, cy = self.centro
        
        for i in range(self.num_nodos):
            fase = (i / self.num_nodos) * 2 * math.pi
            radio = 150 + 30 * math.sin(t * 0.5 + fase * 3)
            
            x = cx + radio * math.cos(t * 0.8 + fase)
            y = cy + radio * math.sin(t * 0.8 + fase)
            
            self.canvas.create_line(cx, cy, x, y, fill="#205000")
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="#76b900")

# --- CONTROLADOR ---
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

# Instanciamos la clase: el código ahora es un objeto que "existe"
ente = Manifestacion(canvas)

def loop():
    ente.dibujar()
    root.after(30, loop)

loop()
root.mainloop()

#oscilador_base.py