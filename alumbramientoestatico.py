import tkinter as tk
import math

WIDTH, HEIGHT = 600, 400
root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#050505")
canvas.pack()

# --- GEOMETRÍA DE ALTO CONTRASTE ---
def dibujar_geometria():
    canvas.delete("all")
    
    # Centro de la proyección
    cx, cy = WIDTH / 2, HEIGHT / 2
    
    # Creamos un sistema de "espejos" para que el logo se vea como una estructura
    # Esto le da un marco de referencia al ojo (adiós al cuadrado blanco)
    for i in range(0, 360, 30):
        rad = math.radians(i)
        # Radio variable para crear una forma 3D (hiperboloide)
        r = 120 + 20 * math.sin(i * 0.1)
        
        x1 = cx + r * math.cos(rad)
        y1 = cy + r * math.sin(rad)
        
        # Dibujamos líneas hacia el centro: ESTO ES EL ANCLA VISUAL
        canvas.create_line(cx, cy, x1, y1, fill="#76b900", width=2)
        # Dibujamos un borde exterior
        canvas.create_oval(x1-5, y1-5, x1+5, y1+5, fill="#ffffff", outline="")

    root.after(50, dibujar_geometria)

dibujar_geometria()
root.mainloop()