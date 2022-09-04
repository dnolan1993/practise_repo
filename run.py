from random import randint

opponent_board = [[" O "] * 8 for x in range(8)]
player_board = [[" O "] * 8 for x in range(8)]

row_list = [1, 2, 3, 4, 5, 6, 7, 8]
column_list = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}


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
    # for ship in range(5):
    ship_row, ship_column = randint(0, 7), randint(0, 7)
    while board[ship_row][ship_column] == " X ":
        ship_row, ship_column = randint(0, 7), randint(0, 7)
    board[ship_row][ship_column] = " X "
    opponent_ship_row.append(ship_row)
    opponent_ship_column.append(ship_column)


def get_ship_row():
    guess_row = int(input("Please guess a row between 1 and 8: "))
    for i in row_list:
        return row_list[guess_row] -2
    while guess_row not in row_list:
        print("Please enter a valid row")
        guess_row = input("Please guess a row between 1 and 8: ")
        return row_list[guess_row] -2


def get_ship_column():
    guess_column = input("Please guess a column A-H: ")
    while guess_column not in column_list.keys():
        print("Please enter a valid column (A-H): ")
        guess_column = input("Please guess a column A-H: ")
    return column_list[guess_column]-1


def hit_ships(board):   
    count = 0
    for row in board:
        for column in row:
            if column == " X ":
                count += 1
    return count


def run_game():
    print("Welcome to Battleship")
    for turns in range(20):
        turns = 20
        while turns > 0:
            print_board(player_board)
            row = get_ship_row()
            column = get_ship_column()
            if row not in opponent_ship_row or column not in opponent_ship_column:
                print("It's a miss!")
                player_board[row][column] = " - "
                turns -= 1
                print(f"You have {turns} turns remaining")
            elif row in opponent_ship_row and column in opponent_ship_column:
                print("Congratulations, It's a hit!")
                player_board[row][column] = " X "
                turns -= 1
                print(f"You have {turns} turns remaining")
            elif player_board[row][column] == " - ":
                print("Positioned already guessed!")
                turns -= 1
                print(f"You have {turns} turns remaining")
            elif hit_ships(player_board) == 1:
                print("All ships have been sunk, Congratulations, You win!")
                break              


def main():
    create_ships(opponent_board)
    print_board(opponent_board)
    print(f"Row {opponent_ship_row}")
    print(f"Column {opponent_ship_column}")
    run_game()
    

main()