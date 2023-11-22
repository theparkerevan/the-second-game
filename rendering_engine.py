import pygame
import layer
import random

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
        # A dictionary that objects can access with their key.
        self.layers = {}

        # Layers sorted by their weight.
        # Will likely only be used to draw the objects in the correct order.
        # Sorted smallest to largest for ease of drawing
        # Low weight means layer is in the back.
        self.weighted_layer_list = []

        self.weighted_layer_list.append(layer.Layer(self.window, "One", random.randint(-50, 50)))
        self.weighted_layer_list.append(layer.Layer(self.window, "Two", random.randint(-50, 50)))
        self.weighted_layer_list.append(layer.Layer(self.window, "Three", random.randint(-50, 50)))
        self.weighted_layer_list.append(layer.Layer(self.window, "Four", random.randint(-50, 50)))
        self.weighted_layer_list.append(layer.Layer(self.window, "Five", random.randint(-50, 50)))
        self.weighted_layer_list.append(layer.Layer(self.window, "Six", random.randint(-50, 50)))

        self.test_layer = layer.Layer(self.window, pygame.surface.Surface((1280, 720)).convert_alpha(), 5)
        

        print("Rendering Engine Created")
    

    def sort(self):
        print("Before")
        for x in self.weighted_layer_list:
            print(x.surface, "-", x.weight)
        print("")

        self.weighted_layer_list = sorted(self.weighted_layer_list, key=lambda x: x.weight)

        print("After")
        for x in self.weighted_layer_list:
            print(x.surface, "-", x.weight)


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