import random


class BoardGame:

    def __init__(self, name, height, width, number_players, piece_markers,end_type,length_to_win):
        self.name = name
        self.width = width
        self.height = height
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]

        self.number_players = number_players
        self.piece_markers = piece_markers
        self.verify_go_each_turn = end_type
        self.length_to_win = length_to_win

