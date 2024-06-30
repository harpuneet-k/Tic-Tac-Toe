board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def check_tie(board):
    for row in board:
        if '' in row:
            return False
    return True

def make_move(board, player, row, col):
    if board[row][col] == '':
        board[row][col] = player
        return True
    else:
        return False
import random

def check_win(board, player):
    # Check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def minimax(board, depth, is_maximizing_player):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    elif check_tie(board):
        return 0

    if is_maximizing_player:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ''
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ''
                    best_score = min(best_score, score)
        return best_score

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = 'X'
                score = minimax(board, 0, False)
                board[row][col] = ''
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)
        
        
def play_game():
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]

    while True:
        print_board(board)

        # Player's move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if not make_move(board, 'O', row, col):
            print("Invalid move, try again.....!!!!")
            continue

        if check_win(board, 'O'):
            print_board(board)
            print()
            print("YOU WIN .....!")
            return

        if check_tie(board):
            print_board(board)
            print()
            print("IT'S A TIE....!")
            return

        # AI's move
        row, col = ai_move(board)
        make_move(board, 'X', row, col)
        print("AI moved to", row, col)

        if check_win(board, 'X'):
            print_board(board)
            print()
            print("AI WINS....!")
            return

play_game()