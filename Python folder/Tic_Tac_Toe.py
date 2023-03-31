def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for row in board:
        print(row)

def is_winner(board, player):
    """Checks if a player has won the game."""
    # Check rows
    for row in board:
        if row == [player, player, player]:
            return True
    # Check columns
    for col in range(3):
        if [board[0][col], board[1][col], board[2][col]] == [player, player, player]:
            return True
    # Check diagonals
    if [board[0][0], board[1][1], board[2][2]] == [player, player, player]:
        return True
    if [board[0][2], board[1][1], board[2][0]] == [player, player, player]:
        return True
    # No winner yet
    return False

def is_board_full(board):
    """Checks if the board is completely filled with X's and O's."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play_game():
    """Plays a game of Tic-Tac-Toe."""
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player = 'X'
    while not is_board_full(board):
        print_board(board)
        row = int(input(f'{current_player}, enter row (1-3): ')) - 1
        col = int(input(f'{current_player}, enter column (1-3): ')) - 1
        if board[row][col] != ' ':
            print('Invalid move, try again!')
            continue
        board[row][col] = current_player
        if is_winner(board, current_player):
            print(f'{current_player} wins!')
            return
        current_player = 'O' if current_player == 'X' else 'X'
    print('Game ends in a tie.')

play_game()
