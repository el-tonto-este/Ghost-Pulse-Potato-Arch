import tkinter as tk
import math

# --- CONFIGURACIÓN ---
WIDTH, HEIGHT = 600, 400
root = tk.Tk()
root.title("Manifestación Cinética")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#050505")
canvas.pack()

# --- ESTADO GLOBAL ---
angulo_rotacion = 0
historial = [] 

def dibujar_geometria():
    global angulo_rotacion, historial
    
    # Fondo con rastro (efecto estela)
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#050505", outline="")
    
    cx, cy = WIDTH / 2, HEIGHT / 2
    num_radios = 18
    puntos_actuales = []
    
    # Calcular puntos actuales
    for i in range(num_radios):
        base_angle = (i * (360 / num_radios)) + angulo_rotacion
        rad = math.radians(base_angle)
        r = 130 + 40 * math.cos(i * 0.3)
        
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        puntos_actuales.append((x, y))
    
    # Dibujar estelas del historial (sin causar error)
    for fotograma in historial:
        for (hx, hy) in fotograma:
            canvas.create_line(cx, cy, hx, hy, fill="#76b900", width=1, stipple="gray25")
            
    # Dibujar la estructura principal
    for (x, y) in puntos_actuales:
        canvas.create_line(cx, cy, x, y, fill="#76b900", width=2)
        canvas.create_oval(x-4, y-4, x+4, y+4, fill="#ffffff", outline="")

    # Actualizar historial
    historial.append(puntos_actuales)
    if len(historial) > 5: # Limitamos a 5 fotogramas de estela
        historial.pop(0)

    # Rotación
    angulo_rotacion += 3
    
    root.after(40, dibujar_geometria)

dibujar_geometria()
root.mainloop()