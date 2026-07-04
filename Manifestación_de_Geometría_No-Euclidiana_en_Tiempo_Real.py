import tkinter as tk
import math

# --- CONFIGURACIÓN DE NÚCLEO ---
WIDTH, HEIGHT = 600, 400
root = tk.Tk()
root.title("Manifestación: Geometría No-Euclidiana")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#050505")
canvas.pack()

# --- GEOMETRÍA ---
num_radios = 18
# Creamos objetos persistentes (Object Pooling) para fluidez absoluta
lineas = [canvas.create_line(0, 0, 0, 0, fill="#205000", width=1) for _ in range(num_radios)]
circulos = [canvas.create_oval(0, 0, 0, 0, fill="#76b900", outline="#ffffff") for _ in range(num_radios)]

angulo_rotacion = 0

def dibujar_geometria():
    global angulo_rotacion
    cx, cy = WIDTH / 2, HEIGHT / 2
    
    for i in range(num_radios):
        # Aceleración armónica: el giro "respira"
        base_angle = (i * (360 / num_radios)) + angulo_rotacion
        rad = math.radians(base_angle)
        
        # Radio asimétrico (forma de hiperboloide)
        r = 130 + 40 * math.cos(i * 0.3)
        
        # Posición
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        
        # Actualización de coordenadas (sin parpadeos)
        canvas.coords(lineas[i], cx, cy, x, y)
        canvas.coords(circulos[i], x-3, y-3, x+3, y+3)

    # La "respiración" cinemática: el ángulo se mueve con un seno
    angulo_rotacion += 1 + math.sin(angulo_rotacion * 0.05) * 2
    
    # Bucle de renderizado a 50 FPS
    root.after(20, dibujar_geometria)

# --- INICIO ---
dibujar_geometria()
root.mainloop()