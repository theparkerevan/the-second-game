import pygame
import directory
import rendering_engine

# The very outer edge of the game
# Holds the main game loop and
# sends off all the important stuff to the game modules.

class TheSecondGame:
    def __init__(self):
        # The game directory
        self.directory = directory.Directory()

        # Game Window
        self.window_width = 1280
        self.window_height = 720

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        
        # Rendering
        self.RenderingEngine = rendering_engine.RenderingEngine(self.directory)
        self.directory.RenderingEngine = self.RenderingEngine

        # Flags
        self.running = True
    

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False


    def run(self):
        while self.running:
            self.eventHandler()