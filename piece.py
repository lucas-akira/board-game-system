class Piece:
    position = (-1,-1)
    marker = 'X'
    owner = None

    def __init__(self, position, marker, owner):
        self.position = position
        self.marker = marker
        self.owner = owner

