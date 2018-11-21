from procedures import Procedures

# This class executes a series of methods from Outcome


class Action:

    def __init__(self, keyboard_input, description, procedure_names, row=[], grid=[], direction = " ", position = (-1,-1)):
        self.keyboard_input = keyboard_input
        self.description = description
        self.procedure_names = procedure_names
        self.row = row
        self.grid = grid
        self.direction = direction
        self.position = position

    def execute(self):
        procedures = Procedures(self.row, self.grid, self.direction, self.position)
        for name in self.procedure_names:
            result = getattr(procedures, name)()
            if name == "add_piece" or name == "remove_piece":
                x,y = self.keyboard_input.split(',')

            else:

                if name == "move_grid":
                    # Update grid for future move_grids, allowing grid movements in a row
                    procedures.grid = result

        # Update grid attribute at the end
        self.grid = result
        return result

    def ask_and_execute(self):
        print(self.description)
        keyboard_input = input()
        if keyboard_input == self.keyboard_input:
            return self.execute()
        else:
            print("Nope")
            return None

grid = [[2,0,0,0], [2, 4, 0, 0], [8, 4, 2, 0], [8, 8, 16, 0]]
#row = [2, 4, 8, 16]
#action = Action("a", "Description Test", ["move_row_left"], row, grid)
action = Action("a", "Put the letter a:", ["move_grid", "move_grid"], grid = grid, direction = "up")
#grid2 = action.ask_and_execute()
#print(grid2)
print(action.grid)

