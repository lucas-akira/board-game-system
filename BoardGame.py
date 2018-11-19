import random

class BoardGame:

    def __init__(self, height, width, players, marker):
        self.width = width
        self.height = height
        self.__grid = [[' ' for i in range(self.width)] for j in range(self.height)]

        self.players = players
        self.__player = [i for i in range(1,self.players+1)]

        self.__marker = marker


    def get_empty_tiles_positions(self):
        empty_position = []
        for i in range(len(game_grid)):
            for j in range(len(game_grid[0])):
                if game_grid[i][j] == 0 or type(game_grid[i][j]) == str:
                    empty_position.append((i, j))
        return empty_position


    def available_position(self, position):
        empty_position = get_empty_tiles_positions(self)
        if position in empty_position:
            return True
        return False


    def display_point(self, x, y, marker):
        self.__grid[x][y] = marker


    def
