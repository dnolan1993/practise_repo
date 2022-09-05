from random import randint

# row_heading = [1, 2, 3, 4, 5, 6, 7, 8]
# column_list = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}

opponent_ship_row = []
opponent_ship_column = []


def print_board(board, opponent=False):
    """ for a given board print it to the terminal """
    
    if opponent:
        print("---------Opponents Board----------")
    else:
        print("-----------Your Board-------------")
    print("    A   B   C   D   E   F   G   H")
    print("----------------------------------")

    row_number = 1
    for row in board:
        col_str = f"{row_number} |"
        for col in row:
                if opponent and col == "#":
                    val = " "
                else:
                    val = col
                col_str += f" {val} |"
        print(col_str)
        row_number += 1

def check_for_oob(board, coordinates ):
    """for a given list of ship coordinates check if any are oob for the board"""
    for i in coordinates:
        if i[0] < 0 or i[0] > len(board)-1: #board is a list of rows
            return True
        elif i[1] < 0 or i[1] > len(board[0])-1: #each row is a list of cols
            return True
    return False

def check_ship_conflict(board, coordinates ):
    """for a given set of coordinates see if they conflict with other ships"""
    for coordinate in coordinates:
        row, col = coordinate[0], coordinate[1]
        if get_coordinate_value(board, row, col) == "#":
            return True
    return False

def check_valid_placement(board, coordinates):
    """Given a board and set of coordinate 
    return if its a valid place to place a ship"""

    if check_for_oob(board, coordinates):
        return False
    elif check_ship_conflict(board, coordinates):
        return False
    
    return True

def get_coordinate_value(board, row, col):
    """for a given board return the value of a coordinate"""
    return board[row][col]

def get_empty_coordinate(board):
    """for a given board find a random empty coordinate"""
    empty = False

    while not empty:
        row, col = randint(0, 7), randint(0, 7)
        coordinate_value = get_coordinate_value(board, row, col)
        if coordinate_value == " ":
            empty = True
    
    return row, col

def get_random_direction():
    """return a random direction"""
    directions = {  0: "up",
                    1:  "down",
                    2: "left",
                    3: "right" }
    
    return  directions[randint(0, 3)]

def generate_ship_coordinates(length, row, col):
    """"given a start point generate a set of coordinates for a ship"""
    
    direction = get_random_direction()
    coordinates = []

    if direction == "up":
        for i in range(length):
            coordinates.append([row - i, col])

    elif direction == "down":
        for i in range(length):
            coordinates.append([row + i, col])

    elif direction == "left":
        for i in range(length):
            coordinates.append([row, col - i])

    else: #right
        for i in range(length):
            coordinates.append([row, col + i])
        
    return coordinates

def place_ship_on_board(board, ship_coordinates):
    """Given a board and a ships coordinates update the board
    with the ship and return the updated board"""
    
    for coordinate in ship_coordinates:
         row, col = coordinate[0], coordinate[1]
         board[row][col] = "#"
    
    return board

def create_ships(board, ships):
    """for a given board place the number of ships required"""
    for i in ships:
        valid_placement = False
        while not valid_placement:
            row, col = get_empty_coordinate(board)
            coordinates = generate_ship_coordinates(i, row, col)
           
            if check_valid_placement(board, coordinates):
                valid_placement = True 

        board = place_ship_on_board(board, coordinates)
    return board

def get_ship_row():
    """
    Allow player to input a guess for row value
    """
    row_heading = [1, 2, 3, 4, 5, 6, 7, 8]
    guess_row = int(input("Please guess a row between 1 and 8: "))
    for i in row_heading:
        return row_heading[guess_row] -2
    while guess_row not in row_heading:
        print("Please enter a valid row")
        guess_row = input("Please guess a row between 1 and 8: ")
        return row_heading[guess_row] -2

def get_ship_column():
    """
    Allow player to input a guess for column value
    """
    column_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    guess_column = input("Please guess a column A-H: ")
    while guess_column not in column_dict.keys():
        print("Please enter a valid column (A-H): ")
        guess_column = input("Please guess a column A-H: ")
    return column_dict[guess_column]-1


def get_player_coordinate():
    """
    Store the players guess as a list
    """
    player_row_column = [get_ship_row() ,get_ship_column()]
    return player_row_column


def get_computer_coordinate():
    """
    Generates random coordinates for computer guess
    """
    computer_row_column = [randint(1,8), randint(1,8)]
    return computer_row_column


def make_a_move(board, coordinate):
    """
    Print guess coordinates to choosen board
    """
    row = coordinate[0]
    col = coordinate[1]
    if get_coordinate_value(board, row, col) == " ":
        print("It's a miss!")
        board[row][col] = "-"
    elif get_coordinate_value(board, row, col) == "#":
        print("Congratulations, It's a hit!")
        board[row][col] = "X"
    elif get_coordinate_value(board, row, col) == "-":
        print("Positioned already guessed!")


def check_win(board):
    """
    Check if all ships have been hit
    """
    if hit_ships(board) == 10:
        print(f"Game Over! all ship on {board} have been sunk!")


def hit_ships(board):  
    """
    Count the amount of hits on chosen board
    """ 
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

def run_game(turns, player_board, opponent_board):
    """Runs the main game loop"""

    while turns > 0:

        coordinate = get_player_coordinate()
        make_a_move(player_board, coordinate)
        if check_win(player_board):
            turns -= 1
            return player_board

        coordinate = get_computer_coordinate()
        make_a_move(opponent_board, coordinate)
        if check_win(opponent_board):
            turns -= 1
            return opponent_board
    
    return None

    # print(f"Welcome to Battleship! You have {turns} to try beat hit as many ships as possible")
    # while turns > 0:
    #     print_board(player_board)
    #     row = get_ship_row()
    #     column = get_ship_column()
    #     if row not in opponent_ship_row or column not in opponent_ship_column:
    #         print("It's a miss!")
    #         player_board[row][column] = " - "
    #         turns -= 1
    #         print(f"You have {turns} turns remaining")
    #     elif row in opponent_ship_row and column in opponent_ship_column:
    #         print("Congratulations, It's a hit!")
    #         player_board[row][column] = " X "
    #         turns -= 1
    #         print(f"You have {turns} turns remaining")
    #     elif player_board[row][column] == " - ":
    #         print("Positioned already guessed!")
    #         print(f"You have {turns} turns remaining")
    #     elif hit_ships(player_board) == 1:
    #         print("All ships have been sunk, Congratulations, You win!")
    #         break
    # print("You have used all your turns, Game Over!")  

def main():

    # this is a list of rows, row is a list of columns
    #  = empty place
    # - = a missed shot
    # * = a hit shot
    # # = location of your ship
    opponent_board = [[" "] * 8 for x in range(8)]
    player_board = [[" "] * 8 for x in range(8)]
    ships = [2,4,4]

    opponent_board = create_ships(opponent_board, ships)
    player_board = create_ships(player_board, ships)

    print_board(opponent_board, opponent=True)
    print_board(player_board)

    winner = run_game(10, player_board, opponent_board)

    print_winner(winner)

    # create_ships(opponent_board)
    # print_board(opponent_board)
    # print(f"Row {opponent_ship_row}")
    # print(f"Column {opponent_ship_column}")
    # run_game()
    

main()