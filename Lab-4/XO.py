class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Menu:
    def display_main_menu(self):
        print("Welcome to X O !")
        print("---------------------------------------------------------------------")
        print("1. Play")
        print("2. Exit")
        while True:
            choice = input("Enter your choice: ")
            if validate_choice(choice):
                return int(choice)
            print("Number must be between 0 and 2")

    def display_endgame_menu(self):
        while True:
            choice = input("\nGame Over!\n1. Restart\n2. Exit\nEnter your choice: ")
            if validate_choice(choice):
                return int(choice)
            print("Number must be between 0 and 2")


def validate_choice(choice):
    return choice.isdigit() and 1 <= int(choice) <= 2


class Board:
    def __init__(self, player1, player2):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = [player1, player2]
        self.current_player = player1

    def display_board(self):
        print("\n  0   1   2")
        for i, row in enumerate(self.board):
            print(i, " | ".join(row))
            if i < 2:
                print("  - + - + - ")

    def get_valid_input(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if 0 <= value <= 2:
                    return value
                else:
                    print("Number must be between 0 and 2")
            except ValueError:
                print("Number must be between 0 and 2")

    def player_move(self):
        while True:
            row = self.get_valid_input(f"{self.current_player.name} ({self.current_player.symbol}), enter row (0-2): ")
            col = self.get_valid_input(f"{self.current_player.name} ({self.current_player.symbol}), enter column (0-2): ")
            
            if self.board[row][col] == " ":
                self.board[row][col] = self.current_player.symbol
                break
            else:
                print("This cell is already taken!")

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def check_tie(self):
        return all(cell != " " for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def play_game(self):
        while True:
            self.display_board()
            self.player_move()
            
            if self.check_winner():
                self.display_board()
                print(f"\n{self.current_player.name} wins!")
                return
            
            if self.check_tie():
                self.display_board()
                print("\nIt's a tie!")
                return

            self.switch_player()

def get_player_info():
    while True:
        p1_name = input("Player 1, enter your name: ")
        if p1_name.isalpha():
            break
        print("Name can only contain letters!")

    while True:
        p1_symbol = input(f"{p1_name}, choose your symbol (X or O): ").upper()
        if p1_symbol in ["X", "O"]:
            break
        print("The symbol must be either 'X' or 'O'")

    while True:
        p2_name = input("\nPlayer 2, enter your name: ")
        if p2_name.isalpha() and p2_name != p1_name:
            break
        print("This name is invalid or already taken!")
    #if a player chooses X, the other player will be assigned O and vice versa
    p2_symbol = "O" if p1_symbol == "X" else "X"
    print(f"{p2_name}, your symbol is '{p2_symbol}'\n")

    return Player(p1_name, p1_symbol), Player(p2_name, p2_symbol)


def main():
    menu = Menu()
    while True:
        choice = menu.display_main_menu()
        if choice == 2:
            print("Goodbye!")
            break

        player1, player2 = get_player_info()
        board = Board(player1, player2)
        board.play_game()

        if menu.display_endgame_menu() == 2:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
