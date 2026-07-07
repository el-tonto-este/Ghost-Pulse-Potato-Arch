import math, time

class UniversoCrudo:
    def __init__(self, w=20, h=10):
        self.w, self.h = w, h
        self.grid = [[0.0 for _ in range(h)] for _ in range(w)]
        self.t = 0

    def tick(self):
        self.t += 0.2
        # El Bosón
        denom = 1 + math.sin(self.t)**2
        x = int((self.w//2) + (self.w//2.5) * math.cos(self.t) / denom)
        y = int((self.h//2) + (self.h//2.5) * math.sin(self.t) * math.cos(self.t) / denom)
        
        # Inyección (Masa fija)
        self.grid[x % self.w][y % self.h] = 10.0
        
        # Entropía (Erosión constante)
        for i in range(self.w):
            for j in range(self.h):
                self.grid[i][j] = max(0.0, self.grid[i][j] - 0.5)

    def render(self):
        # Volcado de datos crudos
        output = ""
        for j in range(self.h):
            for i in range(self.w):
                # Formato fijo para que la matriz no baile
                output += f"{self.grid[i][j]:.1f} "
            output += "\n"
        print(output)

u = UniversoCrudo()
while True:
    u.tick()
    u.render()
    time.sleep(0.1)