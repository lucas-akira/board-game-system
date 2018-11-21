from boardgame import BoardGame
from action import Action

def list_options():
    print("1: Create a new game")
    print("2: Start a new game")
    print("3: Exit")

def positive_int_input():
    repeat = True
    while repeat:
        receiver = input()
        repeat = False
        try:
            receiver = int(receiver)
            if receiver <= 0:
                print("Please enter a positive integer!")
                repeat = True
        except ValueError:
            print("Please enter an integer!")
            repeat = True
    return receiver


def int_input_greater_than_one():
    repeat = True
    while repeat:
        receiver = positive_int_input()
        repeat = False
        if receiver <= 1:
            print("Please enter an integer greater than 1!")
            repeat = True

    return receiver


def create_game_menu():
    repeat = True
    while repeat:
        print("Choose a name for the game:")
        name = input()

        print("Height of the grid:")
        height = int_input_greater_than_one()

        print("Width of the grid:")
        width = int_input_greater_than_one()

        print("Number of players:")
        number_players = positive_int_input()

        piece_markers = []
        print("How many types of pieces?")
        number_types_pieces = positive_int_input()

        for i in range(number_types_pieces):
            print("Marker of piece number {}: (it can't be 0)".format(i+1))
            need_to_ask = True
            while need_to_ask:
                marker = input()
                if marker != "0":
                    need_to_ask = False
                    piece_markers.append(marker)
                else:
                    print("Marker can't be 0! Try again")
                    need_to_ask = True
        print("-------------------------------------")
        print("Recap: ")
        print("Name: {}".format(name))
        print("Grid height: {}".format(height))
        print("Grid width: {}".format(width))
        print("Pieces:")
        for i in range(number_types_pieces):
            print("  Piece number {}: {}".format(i+1, piece_markers[i]))

        print("Everything OK so far? ")
        print("1: Yes, proceed")
        print("2: No, start over again")
        print("3: Go back to menu")
        option = input()

        if option == "1":
            print("Continuing...")
            boardGame = BoardGame(name, height, width, number_players, piece_markers)
            actions = add_turn_actions(boardGame.grid)
            repeat = False
        elif option == "2":
            repeat = True
        elif option == "3":
            repeat = False


def add_turn_actions(grid):
    repeat = True
    while repeat:
        print("What should each player generally do in their turn?")
        print("1: Add individual pieces in empty spaces (e.g: tic-tac-toe)")
        print("2: Try to move all the pieces in the grid in a general position, summing common ones (e.g: 2048)")
        print("3: Go back to menu")
        option = input()
        if option == "1":
            print("Select which keyboard button will correspond ")
            action = Action()
        elif option == "2":
            repeat = True
        elif option == "3":
            return None


def start_menu():
    menu_loop = True
    while menu_loop:
        print("__Board Game__")
        list_options()
        print("Choose an option:")
        option = input()

        if option == "3":
            menu_loop = False
        elif option == "2":
            print("Option 2")
        elif option == "1":
            create_game_menu()
        else:
            print("Invalid option! Try again!")


start_menu()
