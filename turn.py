class Turn:
    player = None
    actions = [] # List of actions
    response = ""

    def list_actions(self):
        print("Player {}'s turn".format(self.player.name))
        print("Available actions:")
        for action in self.actions:
            print("{} : ({})".format(action.description, action.keyboard_input))

    def ask_action(self):
        self.list_actions()
        print("Choose an action:")
        self.response = input()

    def execute_action(self):
        for action in self.actions:
            #if action.keyboard_input == self.response:
                action.execute()
                break
