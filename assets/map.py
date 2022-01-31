


class Cell(object):
    def __init__(self, id):
        self.id = id


class Map(object):
    def __init__(self, rows, columns=None):
        self.board = []
        self.cells = []
        # self.start = [0, 0] # row, col
        # self.exit = [len(self.board), len(self.board[0])] # row, col
        

        # creates a matrix filled with Cells with ids
        id = 1 
        for row in range(rows):
            self.board.append([])
            if columns:
                for col in range(columns):
                    cell = Cell(id)
                    self.board[row].append(cell)
                    self.cells.append(cell)
                    id += 1
            else:
                for col in range(rows):
                    cell = Cell(id)
                    self.board[row].append(cell)
                    self.cells.append(cell)
                    id += 1

        


    def draw_board(self, player_x, player_y):
        """
        Draws the board to the terminal
        """
        wall = "----"
        for row in range(len(self.board)):
            row_to_draw = '|'
            wall_to_draw = ''
            for cell in range(len(self.board[row])):
                if [row, cell] == [player_y, player_x]:
                    row_to_draw = row_to_draw + ' P ' + '|'
                    wall_to_draw = wall_to_draw + wall
                else:
                    row_to_draw = row_to_draw + ' - ' + '|'
                    wall_to_draw = wall_to_draw + wall

            print(wall_to_draw)
            print(row_to_draw)
        for i in range(len(self.board[0])):
            print(wall, end='')
        
        print()


    # def move_player(self):
    #     user_choice = input("Please enter a direction(N,E,S,W): ").upper()

    #     self.previous_x = self.x
    #     self.previous_y = self.y

    #     if user_choice == "N":
    #         self.y = self.y - 1
    #     elif user_choice == "E":
    #         self.x = self.x + 1
    #     elif user_choice == "S":
    #         self.y = self.y + 1
    #     elif user_choice == "W":
    #         self.x = self.x - 1
    #     elif user_choice == "Q":
    #         return True


    # def play_loop(self):
    #     done = False
       
    #     while not done:
    #          self.draw_board()
    #          done = self.move_player()
            

