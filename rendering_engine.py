import pygame
import layer

# Not sure if 'engine' is the right word here, but I think it's silly.
# Hold all the layers, keeps them sorted according to their weights.
# Draws them when asked.

class RenderingEngine:
    def __init__(self, directory, window):
        print("Rendering Engine Called")

        self.directory = directory

        # Giving this the window directly cause it's gonna need it.
        self.window = window

        # Going to need a lot of layers, so make them here.
        self.test_layer = layer.Layer(self.window, pygame.surface.Surface((1280, 720)).convert_alpha(), 5)
        

        print("Rendering Engine Created")
    

    def clearAll(self):
        # Clears all layers by filling them with Clear Color
        self.test_layer.clear()


    def draw(self):
        # Filling window a default background color.
        # Should never be seen
        # Is very green for fast recognition.
        self.window.fill((50, 250, 100))

        self.test_layer.draw()

        # Update Display
        pygame.display.flip()