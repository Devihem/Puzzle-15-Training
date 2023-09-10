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
    for row in range(4):
        for column in range(4):
            if puzzle_grid[row][column] == ' □':
                empty_box_row = row
                empty_box_column = column
                return empty_box_row, empty_box_column


def check_if_puzzle_is_solved(board):
    # puzzle solving pattern
    pattern_grid = [[' 1', ' 2', ' 3', ' 4'], [' 5', ' 6', ' 7', ' 8'], [' 9', '10', '11', '12'],
                    ['13', '14', '15', ' □']]

    if board == pattern_grid:
        return True
    return False


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


# Create the board and randomly place the blocks using .randint
puzzle_grid = create_random_puzzle_board()

# staring variables
row = 0
col = 0

while True:

    # Printing the current stage of the game ( the board )
    printing_the_board(puzzle_grid)

    # Accepting the user input and showing the control
    user_input = user_input_and_control()

    # FINDING ZERO ( mapping ? )
    row, col = finding_empty_box(puzzle_grid)

    # UP
    if user_input == 'W' and row > 0:
        puzzle_grid[row][col], puzzle_grid[row - 1][col] \
            = puzzle_grid[row - 1][col], puzzle_grid[row][col]

    elif user_input == 'S' and row < 3:
        puzzle_grid[row][col], puzzle_grid[row + 1][col] \
            = puzzle_grid[row + 1][col], puzzle_grid[row][col]
    # LEFT
    elif user_input == 'A' and col > 0:
        puzzle_grid[row][col], puzzle_grid[row][col - 1] \
            = puzzle_grid[row][col - 1], puzzle_grid[row][col]

    # RIGHT
    elif user_input == 'D' and col < 3:
        puzzle_grid[row][col], puzzle_grid[row][col + 1] \
            = puzzle_grid[row][col + 1], puzzle_grid[row][col]
        # LEFT

    if check_if_puzzle_is_solved(puzzle_grid):
        print("WINNER")
        print(printing_the_board(puzzle_grid))
        break

# FIX - SOLVABLE OR NOR  - FORMULA
# ADDING - SELF SOLVER
# Terminal VISULATION FIX SOMEHOW
# Common FIX OF CODE FOR GIT HUB
