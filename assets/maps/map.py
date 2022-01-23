


class Cell(object):
    def __init__(self, id):
        self.id = id


class Map(object):
    def __init__(self):
        self.board = []


    def create_board(self, rows, columns=None):
        """
        Creates a board with cell objects
        if columns is None, the number of
        rows will be the same as columns
        """
        id = 1
        for row in range(rows):
            self.board.append([])
            if columns:
                for col in range(columns):
                    cell = Cell(id)
                    self.board[row].append(cell)
                    id += 1
            else:
                for col in range(rows):
                    cell = Cell(id)
                    self.board[row].append(cell)
                    id += 1
    

    def draw_board(self):
        """
        Draws the board to the terminal
        """
        wall = "----"
        for row in self.board:
            row_to_draw = '|'
            wall_to_draw = ''
            for cell in row:
                row_to_draw = row_to_draw + ' - ' + '|'
                wall_to_draw = wall_to_draw + wall
            print(wall_to_draw)
            print(row_to_draw)
        for i in range(len(self.board[0])):
            print(wall, end='')


# my_game = Map()
# my_game.create_board(3, 10)
# my_game.draw_board()