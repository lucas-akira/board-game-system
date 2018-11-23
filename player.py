class Player:

    def __init__(self, name = "default_name"):
        self.name = name
        self.pieces = []  # List of pieces owned
        self.marker = ""  # Marker associated with player
