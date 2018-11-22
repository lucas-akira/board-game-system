import random
from grid import *
from player import Player
from procedures import Procedures
from turn import Turn

class Boardgame:
    piece_marker_dict = {0: " "}
    max_number_players = 0
    players = []
    type = ""  # Options: "2048-like" or "tic-tac-toe-like"

    def __init__(self, name, height, width, max_number_players, end_type, length_to_win):
        self.name = name
        self.width = width
        self.height = height
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]
        self.max_number_players = max_number_players

        # Instantiate a dummy turn object
        self.turn = Turn()

    def g2048_init(self):
        g2048_add_new_tile(self.grid)
        g2048_add_new_tile(self.grid)

    def g2048_after_execution(self, game_over, grid_altered):

        # Procedures object made just to access the methods that test the game over condition
        procedures_obj = Procedures()

        # If the grid was altered, add a new random tile
        if grid_altered:
            g2048_add_new_tile(self.grid)

        # Verify if it's game over
        game_over = procedures_obj.g2048_is_game_over(self.grid)
        max_value = get_grid_tile_max(self.grid)

        if max_value == 2048:
            print("Congratulations! You have a winning configuration!")
        return game_over

    def init_game(self):
        if self.type == "2048-like":
            self.g2048_init()

    def run_game(self):
        # Add players in the game
        for i in range(self.max_number_players):
            print("Player {} name: ".format(i+1))
            new_player = Player(input())
            self.players.append(new_player)
            if i+1 < self.max_number_players:
                print("Do you want to add more players? (You can add {} more)".format(self.max_number_players-i))
                print("1: Yes")
                print("2: No")
                option = input()
                if option == "2":
                    break

        # Start procedure:
        # Put the first player in the list as their turn
        self.turn.player = self.players[0]

        # Run init_game() to load starting situation
        self.init_game()

        # Create game loop
        turn_index = 0 # Variable to keep track of each player's turn
        grid_altered = True # Variable that tells if the grid was altered after an action
        game_over = False
        while not game_over: # Game loop

            # Print the grid
            print(grid_to_string_with_size_and_theme(self.grid, self.piece_marker_dict, len(self.grid)))

            # Announce the player's turn, and their available actions
            self.turn.list_actions()
            # Ask the player which action he/she will perform
            self.turn.ask_action()

            # Execute action
            action_result = self.turn.execute_action()

            # Check if result is valid
            if action_result is not None:
                # If it is, check whether the updated grid is different from the old one
                if not equal_grids(self.grid, action_result):
                    # Update grid
                    self.grid = action_result
                    grid_altered = True
                else:
                    grid_altered = False
            else:
                # Else, the user has put an invalid input (an input that is not equal to any action)
                print("Wrong input! Try again")
                continue

            # Do things after execution (like verify movement)
            if self.type == "2048-like":
                game_over = self.g2048_after_execution(game_over, grid_altered)

            if not game_over:
                # Change turn:
                turn_index += 1
                if turn_index == self.max_number_players:
                    turn_index = 0
                self.turn.player = self.players[turn_index]

        # Print the grid one more time to show the game over grid
        print(grid_to_string_with_size_and_theme(self.grid, self.piece_marker_dict, len(self.grid)))
        print("Game Over !")

        #self.number_players = number_players
        #self.piece_markers = piece_markers
        #self.verify_go_each_turn = end_type
        #self.length_to_win = length_to_win
