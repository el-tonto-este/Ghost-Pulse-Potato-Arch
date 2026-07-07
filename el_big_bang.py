import math, os, time

# Engine: Entropic Lemniscate Universe
# Resolution: 80x40 | Hardware: Potato
class Universe:
    def __init__(self):
        self.w, self.h = 80, 40
        self.grid = [[0.0 for _ in range(self.h)] for _ in range(self.w)]
        self.t = 0

    def tick(self):
        self.t += 0.15
        # Lemniscate driver (The path of the Boson)
        denom = 1 + math.sin(self.t)**2
        x = int((self.w//2) + (self.w//3) * math.cos(self.t) / denom)
        y = int((self.h//2) + (self.h//3) * math.sin(self.t) * math.cos(self.t) / denom)
        
        # Ingestion (Adding "mass")
        self.grid[x % self.w][y % self.h] = 10.0
        
        # Entropy (The decay of everything)
        for i in range(self.w):
            for j in range(self.h):
                self.grid[i][j] = max(0.0, self.grid[i][j] - 0.2)

    def render(self):
        # The "3D-ish" perspective through character density
        chars = " .:-=+*#%@"
        out = "\033[H" # Reset terminal cursor
        for j in range(self.h):
            for i in range(self.w):
                out += chars[int(self.grid[i][j] / 10 * 9)]
            out += "\n"
        print(out)

u = Universe()
while True:
    u.tick()
    u.render()
    time.sleep(0.03)