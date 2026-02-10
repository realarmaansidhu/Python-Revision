# Python Code to practice Class level attributes by creating a Player class with a MAX_POSITION attribute and methods to move and draw the player's position

class Player:
    MAX_POSITION = 10
    
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):
        self.steps = steps
        if (self.position + steps) < Player.MAX_POSITION:
            self.position = self.position + steps
        else:
            self.position = Player.MAX_POSITION
       
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()