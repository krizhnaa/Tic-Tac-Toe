def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # Horizontal win
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # Vertical win
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # Diagonal win
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # Diagonal win
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    tic_tac_toe()