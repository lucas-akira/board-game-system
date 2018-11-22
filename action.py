from procedures import Procedures
from player import Player

# This class executes a series of methods from Outcome


class Action:

    def __init__(self, keyboard_input, description, procedure_names, row=[], grid=[], direction = " ", position = (-1, -1)):
        self.keyboard_input = keyboard_input
        self.description = description
        self.procedure_names = procedure_names
        self.row = row
        self.grid = grid
        self.direction = direction
        self.position = position
        # Initializes a dummy player object
        self.player = Player("No one")

    def execute(self):
        procedures = Procedures(self.row, self.grid, self.direction, self.position)
        # Pass player object to procedures
        procedures.player = self.player

        for name in self.procedure_names:

            if name == "add_piece" or name == "remove_piece":
                # Ask position from the user
                ask_position = True
                while ask_position:
                    # Ask for a position
                    print("Enter a position in the form: x,y")
                    coordinates = input()
                    x = ""
                    y = ""
                    x,y = coordinates.split(',')
                    try:
                        x = int(x)
                        y = int(y)
                        self.position = (x, y)
                        result = getattr(procedures, name)()

                        # If at the method changed self.position to (-1, -1), it means that the given position is invalid
                        # e.g.: can't add piece at an occupied position, or can't remove an empty space
                        if self.position == (-1, -1):
                            # Ask for a new position
                            ask_position = True
                        else:
                            ask_position = False

                    except ValueError:
                        print("Invalid coordinates given! Try again")
                        ask_position = True

            elif name == "move_grid":
                    result = getattr(procedures, name)()
                    # Update grid for future move_grids, allowing grid movements in a row
                    procedures.grid = result
            else:
                return None

        # Update grid attribute at the end
        self.grid = result
        return result

#    def ask_and_execute(self):
#        print(self.description)
#        keyboard_input = input()
#        if keyboard_input == self.keyboard_input:
#            return self.execute()
#        else:
#            print("Nope")
#            return None

#grid = [[2,0,0,0], [2, 4, 0, 0], [8, 4, 2, 0], [8, 8, 16, 0]]
#row = [2, 4, 8, 16]
#action = Action("a", "Description Test", ["move_row_left"], row, grid)
#action = Action("a", "Put the letter a:", ["move_grid", "move_grid"], grid = grid, direction = "up")
#grid2 = action.ask_and_execute()
#print(grid2)
#print(action.grid)

