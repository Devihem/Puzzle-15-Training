import random


def create_random_puzzle_board():
    # Create a random puzzle. If the number is one digit add empty space for better visualisation.
    puzzle = [str(number) if len(str(number)) == 2 else ' ' + str(number) for number in range(16)]

    # Empty box symbol
    puzzle[0] = ' □'

    # Using random.randint for generating different board every new game
    puzzle = [[puzzle.pop(random.randint(0, len(puzzle) - 1)) for _ in range(4)] for _ in range(4)]

    return puzzle


def finding_empty_box(puzzle_grid_map: list):
    return [(r, c) for c in range(4) for r in range(4) if puzzle_grid_map[r][c] == ' □'][0]


def check_if_puzzle_is_solved(board):

    # puzzle solving pattern
    pattern = [[' 1', ' 2', ' 3', ' 4'], [' 5', ' 6', ' 7', ' 8'], [' 9', '10', '11', '12'], ['13', '14', '15', ' □']]

    if board == pattern:
        return True
    return False


def move_the_empty_box(board):
    r, c = finding_empty_box(board)

    # UP
    if user_input == 'W' and r > 0:
        board[r][c], board[r - 1][c] = board[r - 1][c], board[r][c]

    # DOWN
    elif user_input == 'S' and r < 3:
        board[r][c], board[r + 1][c] = board[r + 1][c], board[r][c]

    # LEFT
    elif user_input == 'A' and c > 0:
        board[r][c], board[r][c - 1] = board[r][c - 1], board[r][c]

    # RIGHT
    elif user_input == 'D' and c < 3:
        board[r][c], board[r][c + 1] = board[r][c + 1], board[r][c]

    return board


# -----------------------------PRINTS------------------------------------------------------------
def printing_the_board(puzzle_board: list):
    # Visual representation of the board in terminal
    print(f'\n\n\n\n╔═════╦═════╦═════╦═════╗'
          f'\n║ {"  ║ ".join(puzzle_board[0])}  ║'
          f'\n╠═════╬═════╬═════╬═════╣'
          f'\n║ {"  ║ ".join(puzzle_board[1])}  ║'
          f'\n╠═════╬═════╬═════╬═════╣'
          f'\n║ {"  ║ ".join(puzzle_board[2])}  ║'
          f'\n╠═════╬═════╬═════╬═════╣'
          f'\n║ {"  ║ ".join(puzzle_board[3])}  ║'
          f'\n╚═════╩═════╩═════╩═════╝')


def user_input_and_control():
    # Show the "Game Control" and returning the input
    player_input = input('\n      ╔═════╗      ╔══════╗'
                         '\n      ║  W↑ ║      ║ Enter║ '
                         '\n╔═════╬═════╬═════╗╚══╗   ║'
                         '\n║  ←A ║  S↓ ║  D→ ║   ║   ║'
                         '\n╚═════╩═════╩═════╝   ╚═══╝'
                         '\nKey + Enter -> :')
    return player_input.upper()


# -----------------------------MAIN------------------------------------------------------------

# Create the board and randomly place the blocks using .randint
puzzle_grid = create_random_puzzle_board()

while not check_if_puzzle_is_solved(puzzle_grid):
    # Printing the current state of the board
    printing_the_board(puzzle_grid)

    # User input and control print
    user_input = user_input_and_control()

    # Making the move on the board
    puzzle_grid = move_the_empty_box(puzzle_grid)

print("WINNER")

# FIX - SOLVABLE OR NOR  - FORMULA
# ADDING - SELF SOLVER
# Terminal VISULATION FIX SOMEHOW
# Common FIX OF CODE FOR GIT HUB
