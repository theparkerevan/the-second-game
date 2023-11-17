import directory

# The very outer edge of the game
# Holds the main game loop and
# sends off all the important stuff to the game modules.

class TheSecondGame:
    def __init__(self):
        # The game directory
        self.directory = directory.Directory
    

    def run(self):
        print("Gello Gorld")