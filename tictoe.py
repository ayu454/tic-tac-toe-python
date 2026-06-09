# Tic Tac Toe Game in Python

# Board positions
board = [' ' for _ in range(9)]

# Function to display board
def display_board():
    print("\n")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("\n")

# Function to check winner
def check_winner(player):
    
    # Rows
    if (board[0] == board[1] == board[2] == player or
        board[3] == board[4] == board[5] == player or
        board[6] == board[7] == board[8] == player):
        return True

    # Columns
    if (board[0] == board[3] == board[6] == player or
        board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player):
        return True

    # Diagonals
    if (board[0] == board[4] == board[8] == player or
        board[2] == board[4] == board[6] == player):
        return True

    return False

# Function to check draw
def check_draw():
    return ' ' not in board

# Main game function
def tic_tac_toe():

    current_player = 'X'

    print("TIC TAC TOE")
    print("Positions are as follows:\n")

    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")

    while True:

        display_board()

        try:
            move = int(input(f"Player {current_player}, enter position (1-9): "))

            # Validate input
            if move < 1 or move > 9:
                print("Invalid position! Choose between 1 and 9.")
                continue

            if board[move - 1] != ' ':
                print("Position already taken! Try again.")
                continue

            # Place move
            board[move - 1] = current_player

            # Check winner
            if check_winner(current_player):
                display_board()
                print(f"Player {current_player} wins!")
                break

            # Check draw
            if check_draw():
                display_board()
                print("It's a draw!")
                break

            # Switch player
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

        except ValueError:
            print("Please enter a valid number!")

# Run game
tic_tac_toe()