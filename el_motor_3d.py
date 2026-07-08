import time
import msvcrt

class Incinerador3D_Final:
    def __init__(self, size=30):
        self.size = size
        self.grid = {} 
        self.z_offset = size // 2

    def aplicar_fisica(self):
        nuevos_datos = {}
        for (x, y, z), energia in self.grid.items():
            if energia < 0.05: continue 
            
            # Convección y Difusión (6 direcciones)
            difusion = energia / 6.0
            for dx, dy, dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
                nc = (x+dx, y+dy, z+dz)
                nuevos_datos[nc] = nuevos_datos.get(nc, 0) + difusion
            
            # Enfriamiento (Entropía ajustada al 97%)
            nueva_energia = energia * 0.97
            if nueva_energia > 0.01:
                coords = (x, y, z)
                nuevos_datos[coords] = nuevos_datos.get(coords, 0) + nueva_energia
        self.grid = nuevos_datos

    def render_viewport(self):
        # Mueve el cursor al inicio sin borrar (evita parpadeo)
        output = "\033[H"
        output += f"--- MOTOR TÉRMICO | Z_OFFSET: {self.z_offset} | W/S: Cámara | Q: Salir ---\n"
        
        for y in range(self.size):
            linea = ""
            for x in range(self.size):
                e = self.grid.get((x, y, self.z_offset), 0)
                
                # Shader de Plasma con Fondo de Niebla de Contraste
                if e > 4.0:   r, g, b = 255, 255, 255
                elif e > 2.0: r, g, b = 255, 255, 0
                elif e > 0.8: r, g, b = 200, 50, 0
                elif e > 0.2: r, g, b = 50, 50, 200
                else:         r, g, b = 10, 10, 30 # Fondo Niebla
                
                linea += f"\033[38;2;{r};{g};{b}m█"
            output += linea + "\n"
        print(output, end="")

# --- EJECUCIÓN ---
motor = Incinerador3D_Final(30)
# Limpiamos pantalla al arrancar
print("\033[2J", end="")

try:
    while True:
        # Control de cámara manual
        if msvcrt.kbhit():
            tecla = msvcrt.getch().decode('utf-8', errors='ignore').lower()
            if tecla == 'q': break
            if tecla == 'w': motor.z_offset = min(motor.size - 1, motor.z_offset + 1)
            if tecla == 's': motor.z_offset = max(0, motor.z_offset - 1)

        # Inyección de energía (El núcleo de calor)
        motor.grid[(15, 15, 15)] = 5.0 
        
        motor.aplicar_fisica()
        motor.render_viewport()
        
        time.sleep(0.03)
except KeyboardInterrupt:
    pass
print("\nSimulación finalizada.")