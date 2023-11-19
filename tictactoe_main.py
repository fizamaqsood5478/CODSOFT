import random


def tictactoe_board(board):
    for row in board:
        print("|".join(row))


def is_board_full(board):
    if board is None:
        return False
    return not any(' ' in row for row in board)


def winner(board, player):
    win_states = (
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical winning states
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal winning states
        (0, 4, 8), (2, 4, 6)  # diagonal winning states
    )

    for state in win_states:
        if all(board[i] == player for i in state):
            return True
    return False


def alpha_beta(board, depth, alpha, beta, is_maximizing):
    if winner(board, 'X'):
        return (1, None)
    elif winner(board, 'O'):
        return (-1, None)
    elif is_board_full(board):
        return (0, None)

    if is_maximizing:
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'  # AI
                score, _ = alpha_beta(board, depth - 1, alpha, beta, False)
                board[i] = ' '  # Undo the move for further analysis

                if score > best_score:
                    best_score = score
                    best_move = i
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        if best_move is None:
            return (best_score, None)
        else:
            return (best_score, best_move)

    else:
        best_score = float('inf')
        best_move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # Opponent
                score, _ = alpha_beta(board, depth - 1, alpha, beta, True)
                board[i] = ' '  # Undo the move for further analysis

                if score < best_score:
                    best_score = score
                    best_move = i
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        if best_move is None:
            return (best_score, None)
        else:
            return (best_score, best_move)


def comp_Moves(board):
    _, best_move = alpha_beta(board, 9, -float('inf'), float('inf'), True)
    if best_move is not None:
        board[best_move] = 'X'
    return board


def player_Moves(board):
    while True:
        move = int(input("Enter move (0-8): "))
        if board[move] == ' ':
            board[move] = 'O'
            break
        else:
            print("Invalid move. Try again.")
    return board


def play():
    board = [' '] * 9
    print("Welcome to Tic Tac Toe!")
    print("Here is your board:")
    print("You are 'O' and the computer is 'X'")
    print()

    while True:
        tictactoe_board([board[i:i + 3] for i in range(0, 9, 3)])
        board = player_Moves(board)

        if winner(board, 'O'):
            tictactoe_board([board[i:i + 3] for i in range(0, 9, 3)])
            print("Congratulations! You won!")
            break
        elif is_board_full(board):
            tictactoe_board([board[i:i + 3] for i in range(0, 9, 3)])
            print("It's a tie!")
            break

        board = comp_Moves(board)

        if winner(board, 'X'):
            tictactoe_board([board[i:i + 3] for i in range(0, 9, 3)])
            print("Sorry, you lose!")
            break
        elif is_board_full(board):
            tictactoe_board([board[i:i + 3] for i in range(0, 9, 3)])
            print("It's a tie!")
            break


play()
