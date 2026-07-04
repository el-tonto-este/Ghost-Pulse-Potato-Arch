import tkinter as tk
import math

WIDTH, HEIGHT = 600, 400
root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#050505")
canvas.pack()

num_radios = 18
# Creamos los objetos una sola vez (esto es lo que mata los tirones)
lineas = [canvas.create_line(0, 0, 0, 0, fill="#76b900", width=2) for _ in range(num_radios)]
circulos = [canvas.create_oval(0, 0, 0, 0, fill="#ffffff", outline="") for _ in range(num_radios)]

angulo_rotacion = 0

def dibujar_geometria():
    global angulo_rotacion
    cx, cy = WIDTH / 2, HEIGHT / 2
    
    for i in range(num_radios):
        base_angle = (i * (360 / num_radios)) + angulo_rotacion
        rad = math.radians(base_angle)
        r = 130 + 40 * math.cos(i * 0.3)
        
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        
        # Actualizamos la posición sin borrar ni crear objetos nuevos
        canvas.coords(lineas[i], cx, cy, x, y)
        canvas.coords(circulos[i], x-5, y-5, x+5, y+5)

    angulo_rotacion += 3
    root.after(20, dibujar_geometria) # 20ms = 50 FPS constantes

dibujar_geometria()
root.mainloop()