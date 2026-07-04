import tkinter as tk
import random
import array
import math

# Configuración del "Templo de la Memoria"
MEM_SIZE = 1024
DIM = 32
memoria_viva = array.array('B', [0] * MEM_SIZE)
puntos_control = [[0.0, 0.0] for _ in range(MEM_SIZE)]

def inyectar_caos(event):
    x, y = event.x, event.y
    idx = (x // 20 + (y // 20) * DIM) % MEM_SIZE
    memoria_viva[idx] = (memoria_viva[idx] + 150) % 256
    puntos_control[idx] = [float(x), float(y)]

def bucle_reactor():
    # Difusión (Vasos comunicantes)
    for i in range(1, MEM_SIZE - 1):
        presion = memoria_viva[i] >> 2
        memoria_viva[i-1] = (memoria_viva[i-1] + presion) % 256
        memoria_viva[i+1] = (memoria_viva[i+1] + presion) % 256
        memoria_viva[i] = (memoria_viva[i] - (presion * 2)) % 256
        
        # Actualización de venas
        puntos_control[i][0] += ((i % DIM) * 20 - puntos_control[i][0]) * 0.1
        puntos_control[i][1] += ((i // DIM) * 20 - puntos_control[i][1]) * 0.1

    # Renderizado en el Canvas
    canvas.delete("all")
    for i in range(MEM_SIZE):
        if memoria_viva[i] > 10:
            x1, y1 = puntos_control[i]
            v = memoria_viva[i]
            # Dibujar venas
            color = f"#{int(v):02x}00{int(255-v):02x}"
            canvas.create_line(x1, y1, x1+5, y1+5, fill=color, width=2)
    
    root.after(30, bucle_reactor)

# Ventana Principal
root = tk.Tk()
root.title("Reactor Nativo")
canvas = tk.Canvas(root, width=640, height=640, bg="black")
canvas.pack()
canvas.bind("<Motion>", inyectar_caos)

bucle_reactor()
root.mainloop()