from flask import Flask, render_template, request

app = Flask(__name__)

# Tic-Tac-Toe logic (same as before)
# ... (previous code for game logic)
import math

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner:
        return 1 if winner == 'O' else -1 if winner == 'X' else 0

    empty_cells = get_empty_cells(board)
    if not empty_cells:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)

    empty_cells = get_empty_cells(board)
    for cell in empty_cells:
        board[cell[0]][cell[1]] = 'O'
        score = minimax(board, 0, False)
        board[cell[0]][cell[1]] = ' '

        if score > best_score:
            best_score = score
            best_move = cell

    return best_move

"""
def play_game():
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        print("Welcome to Tic-Tac-Toe!")

        while True:
            print_board(board)
            player_move = input("Enter your move (row[1-3] column[1-3]): ")
            player_row, player_col = map(int, player_move.split())
            player_row -= 1
            player_col -= 1

            if board[player_row][player_col] != ' ':
                print("Invalid move. Try again.")
                continue

            board[player_row][player_col] = 'X'
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Congratulations! {winner} wins!")
                break

            if len(get_empty_cells(board)) == 0:
                print_board(board)
                print("It's a tie!")
                break

            ai_move = best_move(board)
            board[ai_move[0]][ai_move[1]] = 'O'

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"AI wins! Better luck next time.")
                break

            if len(get_empty_cells(board)) == 0:
                print_board(board)
                print("It's a tie!")
                break

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break
"""


# Initialize variables
board = [[' ' for _ in range(3)] for _ in range(3)]
game_over = False

@app.route('/', methods=['GET', 'POST'])
def index():
    global board, game_over

    if request.method == 'POST':
        if not game_over:
            user_move = request.form['move']
            try:
                row, col = map(int, user_move.split(','))
                row -= 1
                col -= 1

                if board[row][col] != ' ':
                    message = "Invalid move. Try again."
                else:
                    board[row][col] = 'X'

                    winner = check_winner(board)
                    if winner:
                        message = f"Congratulations! {winner} wins!"
                        game_over = True
                    elif len(get_empty_cells(board)) == 0:
                        message = "It's a tie!"
                        game_over = True
                    else:
                        ai_move = best_move(board)
                        board[ai_move[0]][ai_move[1]] = 'O'

                        winner = check_winner(board)
                        if winner:
                            message = f"AI wins! Better luck next time."
                            game_over = True
                        elif len(get_empty_cells(board)) == 0:
                            message = "It's a tie!"
                            game_over = True
                        else:
                            message = None
            except ValueError:
                message = "Invalid input format. Enter coordinates as 'row,col'."

        else:
            message = "Game over. Start a new game!"

    else:
        message = None

    return render_template('index.html', board=board, message=message, game_over=game_over)

@app.route('/newgame', methods=['GET','POST'])
def new_game():
    global board, game_over
    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_over = False
    return index()

if __name__ == "__main__":
    app.run(debug=True)
