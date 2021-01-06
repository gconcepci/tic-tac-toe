import random

"""Functions for out Tic Tac Toe game."""
def display_board(board):
    """Displays game board."""
    print('\n'*100)

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')




def player_input():
    """Allows user input to select X or O."""
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1, would you like to be X or O: ").upper()
        if marker == "X":
            return ("X", "O")
        elif marker == "O":
            return ("O", "X")
        else:
            print("Invalid choice.")

def place_marker(board, marker, position):
    """Places marker on board."""
    board[position] = marker

def win_check(board, mark):
    """Checks for a win on the board."""
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # Across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # Across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # Across the bottom
    (board[1] == mark and board[4] == mark and board[7] == mark) or # Down the left
    (board[2] == mark and board[5] == mark and board[8] == mark) or # Down the middle
    (board[3] == mark and board[6] == mark and board[9] == mark) or # Down the right
    (board[1] == mark and board[5] == mark and board[9] == mark) or # Diagonal
    (board[3] == mark and board[5] == mark and board[7] == mark))



def choose_first():
    """Randomly select which player goes first."""
    if random.randint(0,1) == 0:
        return "Player 2"
    else:
        return "Player 1"

def space_check(board, position):
    """Check if a space on the board is free."""
    return board[position] == " "

def full_board_check(board):
    """Check if board is full."""
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    """Let user choose a position for their marker."""
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = input(f"{turn} Please pick a position for marker (1-9): ")
        if position.isdigit():
            position = int(position)
        else:
            print("Invalid choice.")


    return position

def replay():
    """Ask User if they want to play again."""
    choice = ""
    while choice not in ["yes", "no"]:
        choice = input('Do you want to play again? Enter Yes or No: ').lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid choice.")

#------------------------------------------------------------------------------------------------

# GAME LOGIC
while True:
    board = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")

# Welcome Screen
    print("\nWelcome to Tic-Tac-Toe")

# Initialize game
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == "Player 1":
            # Player 1's turn.
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print("Congratulations, Player 1 is the winner!")
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("The game is a draw!")
                break
            else:
                turn = "Player 2"

        if turn == "Player 2":
            # Player 2's turn.
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print("Congratulations, Player 2 is the winner!")
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("The game is a draw!")
                break
            else:
                turn = "Player 1"

    if not replay():
        print("Love you bby")
        break
