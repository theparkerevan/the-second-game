class Layer:
    def __init__(self, window, surface, weight):
        self.window = window
        self.surface = surface
        self.weight = weight

    
    def draw(self):
        self.window.blit(self.surface, (0, 0))