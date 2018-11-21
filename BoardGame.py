import random


class BoardGame:
    piece_marker_dict = {}
    turn = None
    players = []

    def __init__(self, name, height, width):
        self.name = name
        self.width = width
        self.height = height
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]


