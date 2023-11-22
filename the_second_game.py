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
        self.RenderingEngine = rendering_engine.RenderingEngine(self.directory, self.window)
        self.directory.RenderingEngine = self.RenderingEngine

        # Flags
        self.running = True

        # Clock. FPS. Stuff
        self.FPS = 60
        self.clock = pygame.time.Clock()
    

    def eventHandler(self):
        # EVENTS!
        for event in pygame.event.get():
            # Clicking the 'X' in the top right
            if event.type == pygame.QUIT:
                self.running = False
            
            # All Key Presses
            if event.type == pygame.KEYDOWN:
                # Escape Key Quits the game for now.
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                # Using this to test stuff
                if event.key == pygame.K_SPACE:
                    self.RenderingEngine.sort()


    def update(self):
        ...


    def run(self):
        while self.running:
            # Clean slate, artisitcally speaking
            self.RenderingEngine.clearAll()

            # Check for user input and react to it
            self.eventHandler()

            # Update the frame
            self.update()

            # Draw
            self.RenderingEngine.draw()

            # Wait till next frame
            self.clock.tick()