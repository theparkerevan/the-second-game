# Holds references to all the important objects in the game.
# So I don't need to link several things to an object everytime one is made.
# I can instead always link objects the directory.


class Directory:
    def __init__(self):
        print("Directory Called")

        self.RenderingEngine = False
        
        print("Directory Created")