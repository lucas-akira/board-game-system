# File with general grid related functions

import random
from procedures import *


def create_grid(size=4):  # Fonction renvoyant une grille de taille size
    """
    Creates and returns a two-dimensional (size x size) square matrix.

    :param size: Size of the grid (default 4)
    :return: List with "size" elements, each of them a list of "size" elements filled with 0.
    """
    game_grid = []
    for i in range(0, size):
        game_grid.append(size*[0])
    return game_grid


def get_all_tiles(grid):  # Fonction renvoyant la liste des valeurs dans les tuiles
    """
    Creates a simple list with all the elements of game_grid. Any empty spaces (' ') are substituted by zeroes in the list.

    :param grid: The game grid
    :return: List of elements of game_grid, ordered from left-right in a line, up-down column wise
    """
    list_tiles = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ' ':
                list_tiles.append(0)
            else:
                list_tiles.append(grid[i][j])

    return list_tiles


def add_new_tile_at_position(grid, position, value):
    """
    Puts a tile in the game grid, given the coordinates (x,y) of the tile.

    :param grid: The game grid
    :param position: (x, y) tuple with the position
    :param value: The value of the tile (its symbol, for instance)
    :return: Game grid with a new tile with coordinates (x,y)
    """
    grid[position[0]][position[1]] = value

    return grid


def remove_tile_at_position(grid, position):
    grid[position[0]][position[1]] = 0
    return grid


def g2048_add_new_tile_at_position(grid, position):
    """
    Puts 2 or 4 in the game grid, given the coordinates (x,y) of the tile.

    There is a 90% chance that the number will be 2, and 10% that it will be 4.

    :param grid: The game grid
    :param position: (x,y) tuple corresponding to the position
    :return: Game grid with a new number (2 or 4) in the tile with coordinates (x,y)
    """
    number = random.randint(1, 10)
    if number == 1:
        value = 4
    else:
        value = 2
    return add_new_tile_at_position(grid, position, value)


def get_empty_tiles_positions(grid):  # Fonction renvoyant la liste des positions des tuiles vides
    """
    Gets all the empty tiles' coordinates.

    :param grid: The game grid
    :return: List with all the coordinates of empty tiles
    """
    list_empty_positions = []

    for i in range (len(grid)):
        for j in range (len(grid[0])):
            if grid[i][j] == ' ' or grid[i][j] == 0:
                list_empty_positions.append((i,j))

    return list_empty_positions


def grid_get_value(grid, x, y):  # Fonction renvoyant la valeur de la coordonnée x,y de la grille
    """
    Returns the value of the tile at coordinates (x,y). If the value is ' ', returns 0 instead.

    :param grid: The game grid
    :param x: X coordinate of the tile
    :param y: Y coordinate of the tile
    :return: grid[x][y], or 0 if grid[x][y] == ' '
    """
    if grid[x][y]== ' ':
        return 0
    else:
        return grid[x][y]


def g2048_new_position(grid):  # Fonction renvoyant aléatoirement la position d'une tuile vide d'une grille
    """
    Gets the X and Y coordinates of a random empty tile of the grid.

    :param grid: The game grid
    :return: X and Y coordinates of an empty tile
    """
    position_empty_tiles = get_empty_tiles_positions(grid)
    n = len(position_empty_tiles)
    if n > 0:
        return position_empty_tiles[random.randint(0,n-1)]
    else:
        return -1, -1  # On renvoit perdu si il n'y a pas de tuiles vides


def g2048_add_new_tile(grid):
    """
    Puts 2 or 4 in a random empty tile in the grid.

    :param grid: The game grid
    :return: The altered grid with the new tile
    """
    x,y = g2048_new_position(grid)
    return g2048_add_new_tile_at_position(grid, (x, y))


def init_game(size=4):
    """
    Initiates a new 2048 game session. Creates a grid and adds 2 tiles in random positions.

    :param size: The dimension of the square grid
    :return: The game grid
    """
    if size < 2:
        print("Invalid grid size!")
        return None

    game_grid = create_grid(size)
    g2048_add_new_tile(game_grid)
    g2048_add_new_tile(game_grid)
    return game_grid


def create_horizontal_line(string):
    """
    Creates a new formatted string composed of "=" and " " based on parameter "string".
    If there exists a "|" in "string", put a space in its place. Otherwise substitute any other character with "=".

    :param string: Base string
    :return: String composed of "=" and " "
    """
    hor_line = ""
    for letter in string:
        if  letter == "|":
            hor_line += " "
        else:
            hor_line += "="
    return hor_line


def long_value(grid):
    longest = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            length = len(str(grid[i][j]))
            if length > longest:
                longest = length
    return longest


def grid_to_string_with_size(grid, number_lines):
    """
    Creates a string that properly shows the game grid. The string adapts its size depending on the
    max length of the grid elements.

    :param game_grid: The game grid
    :param number_lines: The number of lines of the grid
    :return: String to display the grid
    """
    string = "\n"
    max_element_length = long_value(grid)
    for i in range(number_lines):
        line = " | ".join(str(x).center(max_element_length) for x in grid[i])
        line = "| {} |".format(line)
        horizontal_barrier = create_horizontal_line(line)

        string += "{}\n".format(horizontal_barrier)
        string += "{}\n".format(line)
        string += "{}\n".format(horizontal_barrier)

    return string


def long_value_with_theme(grid, theme_dict):
    """
    Creates a thematic grid based on a dictionary, while also determining the max element length of this new grid.

    :param grid: The game grid
    :param theme_dict: Dictionary that correlates each number on the grid with a theme-specific symbol
    :return: The max element length of the thematic grid, and the new grid itself
    """
    thematic_grid = create_grid(len(grid))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            key = grid[i][j]
            thematic_grid[i][j] = theme_dict[key]
    return long_value(thematic_grid), thematic_grid


def grid_to_string_with_size_and_theme(grid, theme_dict, number_lines):
    """
    Creates a string that properly shows the game grid, based on a theme. The string adapts its size depending on the
    max length of the grid elements.

    :param grid: The game grid
    :param theme_dict: Dictionary that correlates each number on the grid with a theme-specific symbol
    :param number_lines: The number of lines of the grid
    :return: String to display the grid
    """
    max_element_length, thematic_grid = long_value_with_theme(grid, theme_dict)
    return grid_to_string_with_size(thematic_grid, number_lines)


def is_game_over(grid):
    procedures = Procedures()
    if procedures.move_possible(grid) == [False, False, False, False]:
        return True
    else:
        return False


def get_grid_tile_max(grid):
    max_value = 0
    values = get_all_tiles(grid)
    for value in values:
        if value > max_value:
            max_value = value

    return max_value


def equal_grids(grid1, grid2):
    result = False
    if len(grid1) == len(grid2) and len(grid1[0]) == len(grid2[0]):
        result = True
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] != grid2[i][j]:
                    return False

    return result


def is_grid_full(grid):
    is_full = True
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                is_full = False

    return is_full


def transpose_grid(grid):
    grid_t = []
    grid_line = []
    for i in range(len(grid[0])):
        for row in grid:
            grid_line.append(row[i])

        grid_t.append(grid_line)
        grid_line = []
    return grid_t
