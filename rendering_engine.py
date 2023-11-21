import pygame

# Not sure if 'engine' is the right word here, but I think it's silly.
# Hold all the layers, keeps them sorted according to their weights.
# Draws them when asked.

class RenderingEngine:
    def __init__(self, directory):
        print("Rendering Engine Called")

        self.directory = directory
        
        # Going to need a lot of layers, so make them here.
        

        print("Rendering Engine Created")
    

    def draw(self):
        ...