from boardgame import Boardgame
from action import Action
from turn import Turn
import pickle

def list_options():
    print("1: Create a new game")
    print("2: Start a new game")
    print("3: Load games from saved_games.bin")
    print("4: Exit")


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


def create_game_menu(board_list):

    board = None
    actions = None
    repeat = True
    while repeat:
        print("Choose a name for the game:")
        name = input()

        print("Height of the grid:")
        height = int_input_greater_than_one()

        print("Width of the grid:")
        width = int_input_greater_than_one()

        print("Number of players:")
        max_number_players = positive_int_input()

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
        #print("Verify win every turn? (y or n)")
        #end_type=input()
        #print("Length to win:")
        #length_to_win = positive_int_input()

        print("-------------------------------------")
        print("Recap: ")
        print("Name: {}".format(name))
        print("Grid height: {}".format(height))
        print("Grid width: {}".format(width))
        #print("End type: {}".format(end_type))
        #print("Length to win: {}".format(length_to_win))
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

            # Create a new Boardgame Object
            board = Boardgame(name, height, width, max_number_players)

            # But we still need to define the following parameters in this object before we can use the board:
            # - type (defined inside add_turn_actions())
            # - piece_marker_dict
            # - turn (An object of Turn)
            # - players (List of players, will be well defined during game execution rather than creation)
            # At the moment (game creation), we'll define the first three

            # Define piece_marker_dict:
            # Create a dictionary to relate each type of piece with its marker
            marker_dict = {0: " "}

            # To well define the turn object, we need to define a set of actions
            actions = add_turn_actions(board, marker_dict, piece_markers)
            # Verify if list of actions creation was successful
            if actions is not None:
                # Instantiate a turn
                turn = Turn()
                # Define its actions
                turn.actions = actions

                # Then, put it into board as the selected game (Load into menu)
                board.turn = turn

                # Show the created actions
                for action in actions:
                    print("Action: {} with description: {}".format(action.keyboard_input, action.description))

                # Add board into list
                board_list.append(board)

                # Save the created game in a file

                # Try to see if the file already exists
                try:
                    with open("saved_games.bin", "rb") as file_object:
                        # Load board list from file
                        board_list = pickle.load(file_object)

                        # Add newly created game into the loaded list
                        board_list.append(board)
                except FileNotFoundError:
                    print("saved_games.bin not found! Creating...")

                # Save board list:
                try:
                    with open("saved_games.bin", "wb") as file_object:
                        pickle.dump(board_list, file_object)
                except:
                    print("Error trying to create saved_games.bin!")

            repeat = False
        elif option == "2":
            repeat = True
        elif option == "3":
            repeat = False

    return board, actions


def add_turn_actions(board, marker_dict, piece_markers):

    print("What should each player generally do in their turn?")
    print("1: Try to move all the pieces in the grid in a general position, summing common ones (e.g: 2048)")
    print("2: Add individual pieces in empty spaces (e.g: tic-tac-toe)")
    print("3: Go back to menu")
    option = input()
    actions = []
    if option == "1":  # 2048-like game

        # Set the type of the board
        board.type = "2048-like"

        multiple_of_two = 2
        for marker in piece_markers:
            marker_dict[multiple_of_two] = marker
            multiple_of_two *= 2
        # Add dictionary in board object
        board.piece_marker_dict = marker_dict
        print("Correspondence (piece : marker)")
        print(board.piece_marker_dict)

        repeat = True
        while repeat:
            # Ask to add an action:
            print("Actions available: ")
            print("1: Move left")
            print("2: Move up")
            print("3: Move right")
            print("4: Move down")
            print("Which action do you want to add: ")
            action_option = positive_int_input()
            keyboard_input = ""

            if action_option >= 1 and action_option <= 4:
                print("Which key/string do you want to associate this action with? (Write it and press enter)")
                keyboard_input = input()

            if action_option == 1:
                # Instantiate an action
                action = Action(keyboard_input, "Move left", ["move_grid"], grid = board.grid, direction = "left")
                # Add the action in the list
                actions.append(action)
            elif action_option == 2:
                action = Action(keyboard_input, "Move up", ["move_grid"], grid = board.grid, direction = "up")
                # Add the action in the list
                actions.append(action)
            elif action_option == 3:
                action = Action(keyboard_input, "Move right", ["move_grid"], grid = board.grid, direction="right")
                # Add the action in the list
                actions.append(action)
            elif action_option == 4:
                action = Action(keyboard_input, "Move down", ["move_grid"], grid = board.grid, direction="down")
                # Add the action in the list
                actions.append(action)

            ask_to_add = True
            while ask_to_add:
                print("Add another action?")
                print("1: Yes")
                print("2: No")
                option = positive_int_input()
                if option == 1:
                    repeat = True
                    ask_to_add = False
                elif option == 2:
                    repeat = False
                    ask_to_add = False
                else:
                    print("Invalid option! Try again")
                    ask_to_add = True



        # Instantiate an action
        #action = Action("a", "Move left", ["move_grid"], grid = board.grid, direction = "left")
        # Put it in the list of actions
        #actions.append(action)
        # Repeat for each direction
        #action = Action("w", "Move up", ["move_grid"], grid = board.grid, direction = "up")
        #actions.append(action)

        #action = Action("d", "Move right", ["move_grid"], grid = board.grid, direction="right")
        #actions.append(action)

        #action = Action("s", "Move down", ["move_grid"], grid = board.grid, direction="down")
        #actions.append(action)

        return actions

    elif option == "2":  # tic-tac-toe-like game
        # Set the type of the board
        board.type = "tic-tac-toe-like"

        key = 1
        for marker in piece_markers:
            marker_dict[key] = marker
            key += 1
        # Add dictionary in board object
        board.piece_marker_dict = marker_dict
        print("Correspondence (piece : marker)")
        print(board.piece_marker_dict)

        # Ask victory necessary length to win:
        ask_length = True
        while ask_length:
            print("Put the necessary piece length to win the game:")
            length_to_win = positive_int_input()
            if length_to_win <= max(board.height, board.width):
                board.length_to_win = length_to_win
                ask_length = False
            else:
                print("It is impossible to win the game with this length! Try again")
                ask_length = True

        repeat = True
        while repeat:
            print("Actions available: ")
            print("1: Add piece")
            print("2: Remove piece")
            print("Which action do you want to add: ")
            action_option = positive_int_input()
            keyboard_input = ""

            if action_option == 1 or action_option == 2:
                print("Which key/string do you want to associate this action with? (Write it and press enter)")
                keyboard_input = input()

            if action_option == 1:

                ask_piece = True
                chosen_key = 1
                while ask_piece:
                    print("Which piece?")
                    for key, value in marker_dict.items():
                        if key == 0:
                            continue
                        print("Piece number {}: {}".format(key, value))

                    chosen_key = positive_int_input()
                    if chosen_key not in marker_dict.keys():
                        print("No corresponding piece number! Try again")
                        ask_piece = True
                    else:
                        ask_piece = False

                # Instantiate an action
                action = Action(keyboard_input, "Add piece", ["add_piece"], grid = board.grid, value = chosen_key, piece_marker_dict = marker_dict)
                # Add the action in the list
                actions.append(action)

            elif action_option == 2:
                action = Action(keyboard_input, "Remove piece", ["remove_piece"], grid = board.grid)
                # Add the action in the list
                actions.append(action)

            ask_to_add = True
            while ask_to_add:
                print("Add another action?")
                print("1: Yes")
                print("2: No")
                option = positive_int_input()
                if option == 1:
                    repeat = True
                    ask_to_add = False
                elif option == 2:
                    repeat = False
                    ask_to_add = False
                else:
                    print("Invalid option! Try again")
                    ask_to_add = True

        return actions
    elif option == "3":
        return None


def load_game_menu(board_list):
    i = 0
    for board in board_list:
        print("{}: {}".format(i+1, board.name))
        i += 1
    print("Select a game: ")
    option = positive_int_input()
    if option <= i:
        return board_list[option-1]
    else:
        print("Invalid option!")


def start_menu():
    board_list = []
    menu_loop = True
    board = None
    while menu_loop:
        if board is not None:
            print("{} loaded! You can select 2 to play it!".format(board.name))
        print("__Board Game__")
        list_options()
        print("Choose an option:")
        option = input()

        if option == "4":
            menu_loop = False
        elif option == "3":
            try:
                with open("saved_games.bin", "rb") as file_object:
                    # Load board list from file
                    loaded_board_list = pickle.load(file_object)
                    if len(loaded_board_list) > 0:

                        board_list = loaded_board_list
                        # Ask to select which game to load
                        board = load_game_menu(board_list)
                    else:
                        print("File corrupted!")
            except FileNotFoundError:
                print("saved_games.bin not found!")
        elif option == "2":
            # Start created game
            if board is not None:
                board.run_game()
            else:
                print("No game loaded!")
        elif option == "1":
            board,actions = create_game_menu(board_list)
        else:
            print("Invalid option! Try again!")


start_menu()
