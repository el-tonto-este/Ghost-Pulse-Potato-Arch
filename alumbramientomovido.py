import tkinter as tk
import math

WIDTH, HEIGHT = 600, 400
root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#050505")
canvas.pack()

# --- ESTADO DE ROTACIÓN GLOBAL ---
angulo_rotacion = 0

# --- GEOMETRÍA GIRATORIA DE ALTO CONTRASTE ---
def dibujar_geometria():
    global angulo_rotacion
    canvas.delete("all")
    
    # Centro de la proyección
    cx, cy = WIDTH / 2, HEIGHT / 2
    
    # Número de radios para la asimetría (hemos subido a 18 para más detalle)
    num_radios = 18
    
    # Dibujamos los radios del "túnel"
    for i in range(num_radios):
        # El ángulo base ahora se ve afectado por la rotación global
        base_angle = (i * (360 / num_radios)) + angulo_rotacion
        rad = math.radians(base_angle)
        
        # Radio variable para crear la forma 3D (hiperboloide)
        # Usamos math.cos(i * 0.3) para crear una "onda" asimétrica en el radio
        r = 130 + 40 * math.cos(i * 0.3)
        
        x1 = cx + r * math.cos(rad)
        y1 = cy + r * math.sin(rad)
        
        # Dibujamos las líneas del túnel hacia el centro
        canvas.create_line(cx, cy, x1, y1, fill="#76b900", width=2, capstyle=tk.ROUND)
        
        # Dibujamos un borde exterior
        canvas.create_oval(x1-6, y1-6, x1+6, y1+6, fill="#ffffff", outline="")

    # El "Tatuaje" o centro de masa (lo hacemos brillar)
    canvas.create_oval(cx-10, cy-10, cx+10, cy+10, fill="#76b900", outline="#ffffff", width=2)
    
    # --- INCREMENTO DE ROTACIÓN ---
    angulo_rotacion += 2 # Velocidad de giro (prueba con 1 o 5)
    if angulo_rotacion >= 360:
        angulo_rotacion = 0

    # --- BUCLE DE RENDERIZADO DE ALTA EFICIENCIA ---
    # 40ms para aprox 25 FPS (fluido y sin quemar la CPU)
    root.after(40, dibujar_geometria)

# --- INICIO DE LA MANIFESTACIÓN ---
dibujar_geometria()
root.mainloop()