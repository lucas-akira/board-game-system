import random


class BoardGame:

    def __init__(self, name, height, width, number_players, piece_markers):
        self.name = name
        self.width = width
        self.height = height
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]

        self.number_players = number_players
        self.piece_markers = piece_markers
