from action import Action

class Turn:
    player = None
    actions = [] # List of actions
    response = ""

    def __init__(self):
        # Instantiate a dummy Action object as the default value
        self.action_executed = Action('=', "default_description", ["procedure"])

    def list_actions(self):
        print("Player {}'s turn".format(self.player.name))
        print("Available actions:")
        for action in self.actions:
            print("{} : ({})".format(action.description, action.keyboard_input))

    def ask_action(self):
        print("Choose an action:")
        self.response = input()

    def execute_action(self):
        for action in self.actions:
            if action.keyboard_input == self.response:
                self.action_executed = action
                action.execute()
                break
