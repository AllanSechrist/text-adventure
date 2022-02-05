class Tile():
    def __init__(self):
        self.width = 58
        self.height = 58
        self.margin = 2
        self.mapped = False


class EventTile(Tile):
    def __init__(self):
        super().__init__()