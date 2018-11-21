import random
from procedures import Procedures
from grid import *
from player import Player


class Boardgame:
    piece_marker_dict = {0: " "}
    turn = None
    max_number_players = 0
    players = []
    type = ""  # Options: "2048-like" or "tic-tac-toe-like"

    def __init__(self, name, height, width, max_number_players):
        self.name = name
        self.width = width
        self.height = height
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]
        self.max_number_players = max_number_players

    def g2048_init(self):
        g2048_add_new_tile(self.grid)
        g2048_add_new_tile(self.grid)

    def g2048_run(self, game_over):

        # Procedures object made just to access the methods that test the game over condition
        verify_procedures_obj = Procedures()

        # get the direction selected in actual turn
        description = self.turn.action_executed.description
        description_words = description.split()
        direction = description_words[1]

        # Verify if the movement changes the grid
        movements_allowed_list = verify_procedures_obj.move_possible(self.grid)
        verifying_index = 0
        if direction == "left":
            verifying_index = 0
        elif direction == "up":
            verifying_index = 1
        elif direction == "right":
            verifying_index = 2
        elif direction == "down":
            verifying_index = 3

        # If the movement given by the user is valid (changes the grid):
        if movements_allowed_list[verifying_index]:
            # Move the grid
            #self.grid = verify_procedures_obj.move_grid(self.grid, direction)
            self.turn.execute_action()

            # Verify if it's game over (To decide if it should add a new random tile)
            game_over = is_game_over(self.grid)
            if not game_over:
                # If the grid was altered, add a new random tile
                g2048_add_new_tile(self.grid)

            # Verify if it's game over again (To really verify if it is game over)
            game_over = is_game_over(self.grid)
            max_value = get_grid_tile_max(self.grid)

            if max_value == 2048:
                print("Congratulations! You have a winning configuration!")
        # Otherwise, do nothing

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
        turn_index = 0
        game_over = False
        while not game_over: # Game loop

            # Print the grid
            print(grid_to_string_with_size_and_theme(self.grid, self.piece_marker_dict, len(self.grid)))

            # Announce the player's turn, and their available actions
            self.turn.list_actions()
            # Ask the player which action he/she will perform
            self.turn.ask_action()
            ###
            #self.turn.execute_action()

            if self.type == "2048-like":
                self.g2048_run(game_over)

            # Change turn:
            turn_index += 1
            if turn_index == self.max_number_players:
                turn_index = 0
            self.turn.player = self.players[turn_index]

        # Print the grid one more time to show the game over grid
        print(grid_to_string_with_size_and_theme(self.grid, self.piece_marker_dict, len(self.grid)))
        print("Game Over !")

