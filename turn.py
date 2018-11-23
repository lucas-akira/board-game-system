from action import Action
from player import Player


class Turn:
    actions = []  # List of actions
    response = ""

    def __init__(self):
        # Instantiate a dummy Action object as the default value
        self.action_executed = Action("", "default_description", ["procedure"])

        # Instantiate a dummy Player object
        self.player = Player("No one")

        self.piece_marker_dict = {0: " "}

    def list_actions(self):
        print("Player {}'s turn".format(self.player.name))
        print("Available actions:")
        for action in self.actions:
            print("{} : ({})".format(action.description, action.keyboard_input))

    def ask_action(self):
        print("Choose an action:")
        self.response = input()

    def execute_action(self):
        result = []
        for action in self.actions:
            # Check if user has entered a valid input
            if action.keyboard_input == self.response:

                # Add player as the author of the action
                action.player = self.player
                self.action_executed = action
                result = action.execute()
                break

        # If the user did input a valid option, result will be changed (with the updated grid)
        if result:
            # Update all action grids
            for action in self.actions:
                action.grid = result
            return result
        # Else, result will still be an empty list, so return None in this case
        else:
            return None
