import menu

#2 fois fonction transposer
def transpose_grid(grid):
    grid_t = []
    grid_line = []
    for i in range(len(grid[0])):
        for row in grid:
            grid_line.append(row[i])

        grid_t.append(grid_line)
        grid_line = []
    return grid_t


def verify_row(row, necessary_length):
    if len(row) < necessary_length:
        return False, None

    actual_length = 0
    pawn_to_verify = row[0]
    for element in row:
        # Analyse each row
        # Count repeated elements in a row
        if element == pawn_to_verify and element != 0:  # Do not consider 0 an element: it's considered an empty space
            actual_length += 1
            # If the length of these repeated elements reaches the necessary length to victory, stop
            if actual_length == necessary_length:
                # Return true and the winner element
                return True, element
        else:
            actual_length = 1
            pawn_to_verify = element
    return False, None


def verify_grid_rows(grid, necessary_length):
    row_number = 0
    for row in grid:
        is_winner_row, element = verify_row(row, necessary_length)
        if is_winner_row:
            return True, element, row_number

        row_number += 1

    return False, None, -1


def get_backslash_diagonal(grid, uppermost_coordinates):
    """
    Gets the backslash-type diagonal of a grid based on the coordinates of the uppermost element.

    :param grid: The base matrix
    :param uppermost_coordinates: Tuple with the coordinates of the uppermost element of the form (row, column)
    :return: A list of the diagonal elements, starting from the uppermost
    """
    i = uppermost_coordinates[0]
    j = uppermost_coordinates[1]

    diagonal_elements = []
    while i <= len(grid)-1 and j <= len(grid[0])-1:
        # Put it in the list
        diagonal_elements.append(grid[i][j])

        # Go to next element:
        i += 1
        j += 1
    return diagonal_elements


def get_forward_slash_diagonal(grid, uppermost_coordinates):
    """
    Gets the forward slash-type diagonal of a grid based on the coordinates of the uppermost element.

    :param grid: The base matrix
    :param uppermost_coordinates: Tuple with the coordinates of the uppermost element of the form (row, column)
    :return: A list of the diagonal elements, starting from the uppermost
    """
    i = uppermost_coordinates[0]
    j = uppermost_coordinates[1]

    diagonal_elements = []
    while i <= len(grid)-1 and j >= 0:
        # Put it in the list
        diagonal_elements.append(grid[i][j])

        # Go to next element:
        i += 1
        j -= 1
    return diagonal_elements

def victory_by_value(grid, value):
    for line in grid:
        for position in line:
            if position == value:
                return True
    return False

def end_by_board_full(grid): #return True if no more available movement in the grid (for 2048)
    n=len(grid) - 1
    m=len(grid[0]) - 1

    if grid[0][0] == grid[0][1] or grid[0][0] == grid[1][0] :
        return True

    elif grid[0][m] == grid[0][m-1] or grid[0][m] == grid[1][m]:
        return True

    elif grid[n][0] == grid[n-1][0] or grid[n][0] == grid[n][1]:
        return True

    elif grid[n][m] == grid[n][m-1] or grid[n][m] == grid[n-1][m]:
        return True

    else:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and (j != 0 or j != m):
                    if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i+1][j]:
                        return True

                elif i == n and (j != 0 or j != m):
                    if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i-1][j]:
                        return True

                elif j == 0 and (i != 0 or i != n):
                    if grid[i][j] == grid[i-1][j] or grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1]:
                        return True

                elif j == m and (i != 0 or i != n):
                    if grid[i][j] == grid[i-1][j] or grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j-1]:
                        return True

                else:
                    if grid[i][j] == grid[i-1][j] or grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i][j+1]:
                        return True
    return False




def victory(grid, necessary_length, type_victory):
    if type_victory == "1":
        # Horizontal verification
        exists_winner, element, row_number = verify_grid_rows(grid, necessary_length)
        if exists_winner:
            print("Row victory")
            return True, element, row_number

        # Vertical verification
        grid_t = transpose_grid(grid)
        exists_winner, element, column_number = verify_grid_rows(grid_t, necessary_length)
        if exists_winner:
            print("Column victory")
            return True, element, column_number

         # Diagonal verification:

        #   Back slash type diagonals: (\)
        print("Backslash diagonals")

        #       Lower half of the diagonals
        for i in range(len(grid)-1, -1, -1):
            diagonal = get_backslash_diagonal(grid, (i, 0))
            exists_winner, element = verify_row(diagonal, necessary_length)
            if exists_winner:
                print("Diagonal victory")
                return True, element, 0
            print(diagonal)

        #       Upper half of the diagonals
        for j in range(1, len(grid[0])):
            diagonal = get_backslash_diagonal(grid, (0,j))
            exists_winner, element = verify_row(diagonal, necessary_length)
            if exists_winner:
                print("Diagonal victory")
                return True, element, 0
            print(diagonal)

        #   Forward slash type diagonals (/)
        print("Forward slash diagonals")

        #       Upper half of the diagonals
        for j in range(len(grid[0])):
            diagonal = get_forward_slash_diagonal(grid, (0, j))
            exists_winner, element = verify_row(diagonal, necessary_length)
            if exists_winner:
                print("Diagonal victory")
                return True, element, 0
            print(diagonal)

        #       Lower half of the diagonals
        for i in range(1,len(grid)):
            diagonal = get_forward_slash_diagonal(grid, (i, len(grid[0])-1))
            exists_winner, element = verify_row(diagonal, necessary_length)
            if exists_winner:
                print("Diagonal victory")
                return True, element, 0
            print(diagonal)
        return False, None, -1

    elif type_victory == "2":

        if victory_by_value(grid, value):
            print("Victory! Well done")
            return True

        elif end_by_board_full(grid):
            print("Board full, try again!")
            return False

        else:
            return None







grid = [[' ',' ',' ','B',' '],[' ',' ','X','A',' '],[' ','X',' ','A',' '],['X',' ',' ','A','B']]
print(victory(grid, 4))
