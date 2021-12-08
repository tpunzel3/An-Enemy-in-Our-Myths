# This creates an entirely python block separate from the RenPy syntax
init python:
        # Creates the clue class used to create Clue objects
        class Clue:
            # When declaring a Clue, it takes three arguments: name, UI image, and description
            def __init__(self, name, img, desc):
                self.name = name
                self.img = img
                self.desc = desc
