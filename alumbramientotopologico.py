import tkinter as tk
import math

# --- CONFIGURACIÓN DE NÚCLEO ---
WIDTH, HEIGHT = 600, 400
root = tk.Tk()
root.title("Manifestación del Silicio: Driver Cinético")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#050505")
canvas.pack()

# --- GEOMETRÍA ---
num_radios = 18
# Creamos objetos persistentes para eliminar tirones (Object Pooling)
lineas = [canvas.create_line(0, 0, 0, 0, fill="#205000", width=1) for _ in range(num_radios)]
circulos = [canvas.create_oval(0, 0, 0, 0, fill="#76b900", outline="#ffffff") for _ in range(num_radios)]

angulo_rotacion = 0

def dibujar_geometria():
    global angulo_rotacion
    cx, cy = WIDTH / 2, HEIGHT / 2
    
    for i in range(num_radios):
        # Cálculo de rotación dinámica
        base_angle = (i * (360 / num_radios)) + angulo_rotacion
        rad = math.radians(base_angle)
        
        # Radio asimétrico (la "forma" del logo)
        r = 130 + 40 * math.cos(i * 0.3)
        
        # Posición final
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        
        # Actualización de coordenadas (sin borrar el lienzo = Cero Tirones)
        canvas.coords(lineas[i], cx, cy, x, y)
        canvas.coords(circulos[i], x-3, y-3, x+3, y+3)

    # Incremento de giro
    angulo_rotacion += 2
    if angulo_rotacion >= 360:
        angulo_rotacion = 0
        
    # Lazo de renderizado fluido
    root.after(20, dibujar_geometria)

# --- INICIO ---
dibujar_geometria()
root.mainloop()