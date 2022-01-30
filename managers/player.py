


class PlayerManager():
    def __init__(self):
        self.x = 0
        self.y = 0
    
        self.previous_x = 0
        self.previous_y = 0

    def move_player(self):
        user_choice = input("Please enter a direction(N,E,S,W): ").upper()

        self.previous_x = self.x
        self.previous_y = self.y

        if user_choice == "N":
            self.y = self.y - 1
        elif user_choice == "E":
            self.x = self.x + 1
        elif user_choice == "S":
            self.y = self.y + 1
        elif user_choice == "W":
            self.x = self.x - 1
        elif user_choice == "Q":
            return True
        


