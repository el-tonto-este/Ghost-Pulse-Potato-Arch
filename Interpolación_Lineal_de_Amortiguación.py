import tkinter as tk
import math

# --- CONFIGURACIÓN ---
WIDTH, HEIGHT = 600, 400
root = tk.Tk()
root.title("Manifestación: Flujo Orgánico")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#050505")
canvas.pack()

num_radios = 18
lineas = [canvas.create_line(0, 0, 0, 0, fill="#205000", width=1) for _ in range(num_radios)]
circulos = [canvas.create_oval(0, 0, 0, 0, fill="#76b900", outline="#ffffff") for _ in range(num_radios)]

# Estado para LERP (Posiciones actuales de los puntos)
pos_actual = [(WIDTH/2, HEIGHT/2) for _ in range(num_radios)]
angulo_rotacion = 0

def dibujar_geometria():
    global angulo_rotacion, pos_actual
    cx, cy = WIDTH / 2, HEIGHT / 2
    
    angulo_rotacion += 1 + math.sin(angulo_rotacion * 0.05) * 2
    
    for i in range(num_radios):
        # 1. Calcular dónde DEBERÍA estar el punto (la meta)
        base_angle = (i * (360 / num_radios)) + angulo_rotacion
        rad = math.radians(base_angle)
        r = 130 + 40 * math.cos(i * 0.3)
        meta_x = cx + r * math.cos(rad)
        meta_y = cy + r * math.sin(rad)
        
        # 2. LERP: Moverse un 15% hacia la meta (suavizado)
        # Esto elimina los tirones y crea el efecto de "flotación"
        cur_x, cur_y = pos_actual[i]
        new_x = cur_x + (meta_x - cur_x) * 0.15
        new_y = cur_y + (meta_y - cur_y) * 0.15
        pos_actual[i] = (new_x, new_y)
        
        # 3. Dibujar
        canvas.coords(lineas[i], cx, cy, new_x, new_y)
        canvas.coords(circulos[i], new_x-3, new_y-3, new_x+3, new_y+3)

    root.after(20, dibujar_geometria)

dibujar_geometria()
root.mainloop()