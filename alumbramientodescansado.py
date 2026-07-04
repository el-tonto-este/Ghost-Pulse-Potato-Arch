import tkinter as tk
import math

WIDTH, HEIGHT = 600, 400
root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#050505")
canvas.pack()

angulo_rotacion = 0
# Historial para las estelas (nodos anteriores)
historial = [] 

def dibujar_geometria():
    global angulo_rotacion, historial
    
    # EFECTO DE DESVANECIMIENTO (La "leucemia" controlada)
    # En lugar de borrar todo, pintamos un rectángulo negro con transparencia
    # (Simulado dibujando un negro semi-transparente sobre todo)
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#050505", outline="", stipple="gray25")
    
    cx, cy = WIDTH / 2, HEIGHT / 2
    num_radios = 18
    puntos_actuales = []
    
    for i in range(num_radios):
        base_angle = (i * (360 / num_radios)) + angulo_rotacion
        rad = math.radians(base_angle)
        r = 130 + 40 * math.cos(i * 0.3)
        
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        
        # Dibujar estelas del historial
        for (hx, hy) in historial[-5:]: # Los últimos 5 frames
            canvas.create_line(cx, cy, hx, hy, fill="#76b900", width=1, stipple="gray50")
            
        canvas.create_line(cx, cy, x, y, fill="#76b900", width=2)
        puntos_actuales.append((x, y))

    historial.append(puntos_actuales)
    if len(historial) > 10: historial.pop(0)

    angulo_rotacion += 3
    root.after(30, dibujar_geometria)

dibujar_geometria()
root.mainloop()