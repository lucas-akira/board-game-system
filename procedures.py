import copy
from grid import *
# All non-static public methods will try to execute based on the parameters given,
# but if no parameters are given, then these methods will use the class attributes instead


class Procedures:

    # Attributes:
    row = []
    grid = []
    direction = " "
    position = (-1,-1)

    def __init__(self, row=[], grid=[], direction="", position=(-1,-1)):
        self.row = row
        self.grid = grid
        self.direction = direction
        self.position = position

    # 2048 Methods:

    def sum_row_left(self, row = []):
        if row == []:
            row = self.row

        n = len(row)
        for i in range(0, n-1):
            if row[i] != 0 and row[i] == row[i+1]:
                row[i] = row[i] + row[i+1]
                row[i+1] = 0
        return row

    def offset_row_left(self, row):
        if row == []:
            row = self.row

        n = len(row)
        for i in range(0,n-1):
            if row[i] == 0:
                # Count the number of zeroes to the right of the tile (variable j)
                for j in range(i, n):
                    # Verify if there is any non-zero tile in the way
                    if row[j] != 0:
                        break

                if row[j] != 0:
                    row[i], row[j] = row[j], row[i]

        return row

    def move_row_left(self, row = []):
        if row == []:
            row = self.row

        row = self.offset_row_left(row)
        row = self.sum_row_left(row)
        row = self.offset_row_left(row)
        return row

    def move_row_right(self, row = []):
        if row == []:
            row = self.row

        row.reverse()
        row = self.move_row_left(row)
        row.reverse()
        return row

    def move_grid(self, grid = [], direction = " "):
            if grid == []:
                grid = self.grid

            if direction == " ":
                direction = self.direction

            # Create a deep copy of the grid so that the moves do not change the original grid
            grid_to_modify = copy.deepcopy(grid)

            if direction == "left":
                for row in grid_to_modify:
                    self.move_row_left(row)
            elif direction == "right":
                for row in grid_to_modify:
                    self.move_row_right(row)
            elif direction == "up":
                grid_t = transpose_grid(grid_to_modify)
                for row in grid_t:
                    self.move_row_left(row)
                grid_to_modify = transpose_grid(grid_t)
            elif direction == "down":
                grid_t = transpose_grid(grid_to_modify)
                for row in grid_t:
                    self.move_row_right(row)
                grid_to_modify = transpose_grid(grid_t)

            return grid_to_modify

    def move_possible(self, grid = []):
        directions = ["left", "up", "right", "down"]
        result_list = []  # In order: [Left, Up, Right, Down]
        # Create a deep copy of the grid so that the test moves do not change the original grid
        grid_to_modify = copy.deepcopy(grid)

        for direction in directions:
            grid_to_modify = self.move_grid(grid_to_modify, direction)

            # If the grid after the movement is identical to it before the movement, the movement is not possible
            if equal_grids(grid, grid_to_modify):
                result_list.append(False)
            else:  # Otherwise movement is possible
                result_list.append(True)
                # Undo the movement for the next test
                grid_to_modify = copy.deepcopy(grid)

        return result_list

    # Tic-tac-toe methods:
    def add_piece(self, type, owner):
        if is_grid_full(self.grid):
            return False

        empty_spaces = get_empty_tiles_positions(self.grid)
        if self.position in empty_spaces:
            add_new_tile_at_position(self.grid, self.position, type)
            return True
        else:
            return False

    def remove_piece(self):
        empty_spaces = get_empty_tiles_positions(self.grid)
        if self.position not in empty_spaces:
            remove_tile_at_position(self.grid, self.position)
            return True
        else:
            return False

    def g2048_is_game_over(self, grid):
        if self.move_possible(grid) == [False, False, False, False]:
            return True
        else:
            return False
