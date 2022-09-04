from random import randint

opponent_board = [[" O "] * 8 for x in range(8)]
player_board = [[" O "] * 8 for x in range(8)]

row_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
column_list = ["A", "B", "C", "D", "E", "F", "G", "H"]


def print_board(board):
    print("  A   B   C   D   E   F   G   H")
    print("  -----------------------------")
    row_number = 1
    for row in board:
        print("{0}{1}"  .format(row_number, "|".join(row)))
        row_number += 1


opponent_ship_row = []
opponent_ship_column = []


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == " X ":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = " X "
        opponent_ship_row.append(ship_row)
        opponent_ship_column.append(ship_column)


def get_ship_row():
    guess_row = input("Please guess a row between 1 and 8: ")
    for i in row_list:
        return i
    while guess_row not in i:
        print("Please enter a valid row")
        guess_row = input("Please guess a row between 1 and 8: ")
    return int(guess_row) 


def get_ship_column():
    guess_column = input("Please guess a column A-H: ")
    while guess_column not in column_list:
        print("Please enter a valid column (A-H): ")
        guess_column = input("Please guess a column A-H: ")
    return guess_column.upper()


def hit_ships(board):
    count = 0
    for row in board(board):
        for column in row:
            if column == "X":
                count += 1
    return count


def run_game():
    turns = 20
    for turns in range(20):
        while turns > 0:
            print("Welcome to Battleship")
            print_board(player_board)
            row = get_ship_row()
            column = get_ship_column()
            if row != opponent_ship_row and column != opponent_ship_column:
                print("It's a miss!")
                player_board[row][column] = "-"
                turns -= 1
            elif row == opponent_ship_row and column == opponent_ship_column:
                print("Congratulations, It's a hit!")
                player_board[row][column] = "X"
                turns -= 1
            elif player_board[row][column] == "-":
                print("Positioned already guessed!")
                turns -= 1
            if hit_ships(player_board) == 5:
                print("All ships have been sunk, Congratulations, You win!")
                break
            print(f"You have {turns} turns remaining")
            if turns == 0:
                print("Game Over")
                break


def main():
    create_ships(opponent_board)
    print_board(opponent_board)
    print(opponent_ship_row)
    print(opponent_ship_column)
    run_game()
    

main()