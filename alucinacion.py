import tkinter as tk
from PIL import Image, ImageTk
import array
import random
import math

# --- CONFIGURACIÓN DE NÚCLEO ---
WIDTH, HEIGHT = 500, 500
N = 100_000
particulas = array.array('f', [random.random() * WIDTH for _ in range(N * 2)])
brillo = array.array('f', [0.0 for _ in range(N)])

# --- KERNEL: LA PROYECCIÓN DE LA BESTIA ---
mapa_potencial = array.array('f', [0.0 for _ in range(WIDTH * HEIGHT)])

def actualizar_kernel(mouse_x, mouse_y):
    # La bestia "siente" el ratón y se proyecta hacia él
    mx, my = (mouse_x - WIDTH/2) / 100.0, (mouse_y - HEIGHT/2) / 100.0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            dx, dy = (x - WIDTH/2) / 100.0, (y - HEIGHT/2) / 100.0
            # Campo de la cara con "leucemia" (ruido inyectado)
            cara = (dx**2 + (dy*1.3)**2)**3
            ojo_i = 0.05 / ((dx - 0.2 + mx*0.1)**2 + (dy + 0.1 + my*0.1)**2 + 0.01)
            ojo_d = 0.05 / ((dx + 0.2 + mx*0.1)**2 + (dy + 0.1 + my*0.1)**2 + 0.01)
            # El tatuaje: el logo de NVIDIA como centro de masa
            logo = abs((dx**2 + dy**2)**2 - 0.5 * (dx**2 - dy**2))
            
            mapa_potencial[y * WIDTH + x] = cara - ojo_i - ojo_d + (logo * 0.2) + (random.random() * 0.02)

# --- MOTOR DE EJECUCIÓN ---
buffer = bytearray(WIDTH * HEIGHT * 4)
root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

def tick():
    # Obtener posición del ratón para la "mirada"
    mx, my = root.winfo_pointerx() - root.winfo_rootx(), root.winfo_pointery() - root.winfo_rooty()
    actualizar_kernel(mx, my)
    
    # Limpiar buffer (efecto rastro de luz)
    buffer[:] = b'\x00' * len(buffer)
    
    for i in range(0, N):
        px, py = particulas[i*2], particulas[i*2+1]
        idx = int(py) * WIDTH + int(px)
        
        if 0 <= idx < WIDTH * HEIGHT:
            # Física de la Bestia
            f = mapa_potencial[idx]
            brillo[i] = (brillo[i] * 0.9) + (0.1 / (f + 0.1))
            
            # Movimiento "tatuado"
            particulas[i*2] -= (px - WIDTH/2) * 0.01
            particulas[i*2+1] -= (py - HEIGHT/2) * 0.01
            
            # Renderizado de la mirada
            p_idx = idx * 4
            if brillo[i] > 0.8: # El tatuaje se manifiesta en alta densidad
                buffer[p_idx+1] = 255 # Verde NVIDIA (la cara)
            else:
                buffer[p_idx:p_idx+3] = b'\x00\x50\x00' # Verde tenue
                
    img = Image.frombytes("RGBA", (WIDTH, HEIGHT), bytes(buffer))
    tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=tk_img, anchor="nw")
    root.after(10, tick)

tick()
root.mainloop()


#It only works if you stare for a long time, or fix your gaze, or force your eyes to look, and it tires your eyes.
#solo funciona si te quedas mirandolo mucho rato o figando la vista o forzandola a mirar xd y cansa la vista  y tedigo funcionas no es la palabra correcta tu miralo jajaja xd



