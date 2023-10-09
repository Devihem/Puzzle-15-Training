from random import randint


def printing_the_board(p_board: list, size):
    # Visual representation of the board in terminal
    for row in range(size):

        # Step 1 Board Row
        if row == 0:
            print(f'\n\n\n\n╔{"═════╦" * (size - 1)}═════╗')
        else:
            print(f'╠{"═════╬" * (size - 1)}═════╣')

        # Step 2 Numbers Row
        print(f'║ {"  ║ ".join([str(num) if len(str(num)) == 2 else " " + str(num) for num in p_board[row]])}  ║')

        # Step 3 Final Board Row
        if row == size - 1:
            print(f'╚{"═════╩" * (size - 1)}═════╝')


def printing_user_control():
    # Show the "Game Control".
    print('\n      ╔═════╗      ╔══════╗'
          '\n      ║  W↑ ║      ║ Enter║ '
          '\n╔═════╬═════╬═════╗╚══╗   ║'
          '\n║  ←A ║  S↓ ║  D→ ║   ║   ║'
          '\n╚═════╩═════╩═════╝   ╚═══╝')


# Receiving One or More direction-command in string and moving the empty box
def move_the_empty_box(board, size, commands_string):
    for command in commands_string:
        r, c = finding_empty_box(board, size)

        # UP
        if command.upper() == 'W' and r > 0:
            board[r][c], board[r - 1][c] = board[r - 1][c], board[r][c]

        # DOWN
        elif command.upper() == 'S' and r < size - 1:
            board[r][c], board[r + 1][c] = board[r + 1][c], board[r][c]

        # LEFT
        elif command.upper() == 'A' and c > 0:
            board[r][c], board[r][c - 1] = board[r][c - 1], board[r][c]

        # RIGHT
        elif command.upper() == 'D' and c < size - 1:
            board[r][c], board[r][c + 1] = board[r][c + 1], board[r][c]

    return board


# Return Tuple(r,c) - Giving the location of the EMPTY BOX
def finding_empty_box(p_board, size):
    return [(r, c) for c in range(size) for r in range(size) if p_board[r][c] == ' □'][0]


# Check if the puzzle is SOLVED
def puzzle_solve_check(board, size):
    flattened_board = flattened_matrix_in_list(board)
    result = all([True if flattened_board[index] == index + 1 else False for index in range(len(flattened_board) - 1)])
    return result


# Flatten 2D matrix to List.
def flattened_matrix_in_list(matrix):
    flattened_matrix = [item for row in matrix for item in row]
    return flattened_matrix


# Ask the user for new game, before quit
def new_game():
    return False


# Create the puzzle based on size and arrange it in matrix
def create_puzzle(size):
    while True:
        b_gen = [number for number in range(size ** 2)]
        b_gen[0] = ' □'
        b_gen = [[b_gen.pop(randint(0, len(b_gen) - 1)) for _ in range(size)] for _ in range(size)]

        if puzzle_is_solvable(b_gen, size):
            break

    return b_gen


def puzzle_is_solvable(b_gen, size):
    flat_matrix = flattened_matrix_in_list(b_gen)
    number_of_inversions = 0
    box_row, box_col = finding_empty_box(b_gen, size)

    # TODO. Maybe is possible to remove the symbol   from the array before check and to make it in comprehension

    # Going and compare all numbers in the array for Any Pair where A is before B. If A > B Inversions + 1!
    for a_numb_index in range((size ** 2) - 1):
        a_numb = flat_matrix[a_numb_index]
        for b_numb_index in range(a_numb_index + 1, size ** 2):
            b_numb = flat_matrix[b_numb_index]
            if type(a_numb) == type(b_numb):
                if a_numb > b_numb:
                    number_of_inversions += 1

    # Option 1 - N(size) is ODD and Inversion must be ODD
    if size % 2 == 1 and number_of_inversions % 2 == 1:
        return True

    # Option 2 - N(size) is ODD. Then there is two options !
    elif size % 2 == 0:

        # Option 2.1 Empty box on ODD row (count from bottom) and Inversion must be EVEN
        if box_row % 2 == 1 and number_of_inversions % 2 == 0:
            return True

        # Option 2.2 Empty box on EVEN row (count from bottom) and Inversion must be ODD
        elif box_row % 2 == 0 and number_of_inversions % 2 == 1:
            return True
        # Every other option is not solvable !
        else:
            return False
    else:
        return False


# ------------------------------------MAIN--------------------------------------------

puzzle_size = int(input("Select Puzzle Size [3-10] ?"))

# !!! Gaming repeater
while True:

    puzzle_board = create_puzzle(puzzle_size)

    while not puzzle_solve_check(puzzle_board, puzzle_size):
        printing_the_board(puzzle_board, puzzle_size)

        printing_user_control()

        command_input = input("Key + Enter -> :")

        move_the_empty_box(puzzle_board, puzzle_size, command_input)

    print('YOU WIN')

    if not new_game():
        print("END GAME")
        break
