# Simple Tic-Tac-Toe Game

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([spot == player for spot in board[i]]):  # Row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full (for a draw)
def check_draw(board):
    return all([cell != " " for row in board for cell in row])

# Main function to run the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Get player input
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] != " ":
                print("This spot is taken. Choose another.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        # Update the board and print it
        board[row][col] = current_player
        print_board(board)
        
        # Check for win or draw
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
