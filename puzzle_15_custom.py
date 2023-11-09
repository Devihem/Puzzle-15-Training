if __name__ == '__main__':  # Q?
    from random import randint
    from solver_assistant import SolverAssistant
    from copy import deepcopy


# ----------------------------------------------------PRINTS------------------------------------------------------------
def printing_the_board(p_board: list, size):
    # Visual representation of the board in terminal
    for row in range(size):

        # Step 1 Board Row
        if row == 0:
            print(f'\n\n╔{"═════╦" * (size - 1)}═════╗')
        else:
            print(f'╠{"═════╬" * (size - 1)}═════╣')

        # Step 2 Numbers Row
        print(f'║ {"  ║ ".join([str(num) if len(str(num)) == 2 else " " + str(num) for num in p_board[row]])}  ║')

        # Step 3 Final Board Row
        if row == size - 1:
            print(f'╚{"═════╩" * (size - 1)}═════╝')


def printing_user_control(m_l, m_r, m_u, m_d):
    # Show the "Game Control".
    print('\n      ╔═════╗      ╔═════╗ ╔═════╗ ╔═════╗ ╔══════╗'
          f'\n      ║  {m_u}↑ ║      ║  H  ║ ║  P  ║ ║  F  ║ ║ Enter║ '
          '\n╔═════╬═════╬═════╗╚═════╝ ╚═════╝ ╚═════╝ ╚══╗   ║'
          f'\n║  ←{m_l} ║  {m_d}↓ ║  {m_r}→ ║                           ║   ║'
          '\n╚═════╩═════╩═════╝                           ╚═══╝')


# --------------------------------------------------FUNCTIONS-----------------------------------------------------------
# Ask the user for new game, before quit
def new_game():
    while True:
        new_game_input = input("Do you want to play another game ? Y/N")
        if new_game_input.upper() == "Y":
            return True
        elif new_game_input.upper() == "N":
            return False


# Create the puzzle based on size and arrange it in matrix. Return SOLVABLE version of the puzzle.
def create_puzzle(size, box_symbol):
    while True:
        puzzle_generated = [number for number in range(size ** 2)]
        puzzle_generated[0] = box_symbol
        puzzle_generated = [[puzzle_generated.pop(
            randint(0, len(puzzle_generated) - 1)) for _ in range(size)] for _ in range(size)]

        # If RANDOM puzzle is not solvable create NEW
        if check_if_puzzle_is_solvable(puzzle_generated, size, box_symbol):
            break

    return puzzle_generated


def check_if_puzzle_is_solvable(puzzle_generated, size, box_symbol):
    flat_matrix = flattened_matrix_in_list(puzzle_generated)
    number_of_inversions = 0
    box_row, box_col = find_element_location(puzzle_generated, size, box_symbol)

    # Going and compare all numbers in the array for Any Pair where A is before B. If A > B Inversions + 1!
    for a_numb_index in range((size ** 2) - 1):
        a_numb = flat_matrix[a_numb_index]

        for b_numb_index in range(a_numb_index + 1, size ** 2):
            b_numb = flat_matrix[b_numb_index]

            if type(a_numb) is type(b_numb):
                if a_numb > b_numb:
                    number_of_inversions += 1

    # N(size) is ODD
    if size % 2 == 1:

        # SOLVABLE if Inversion is ODD
        if number_of_inversions % 2 == 0:
            return True

        # Every other combination is not solvable !
        else:
            return False

    # N(size) is EVEN.
    elif size % 2 == 0:

        # SOLVABLE if Inversion is EVEN and Empty box os on ODD row (count from bottom)
        if box_row % 2 == 1 and number_of_inversions % 2 == 0:
            return True

        # SOLVABLE if Inversion is ODD and Empty box os on EVEN row (count from bottom)
        elif box_row % 2 == 0 and number_of_inversions % 2 == 1:
            return True

        # Every other combination is not solvable !
        else:
            return False


# Receiving command string and move the empty box in the needed directions.
def move_the_empty_box(m_left, m_right, m_up, m_down, board, size, box_symbol, commands_string):
    for command in commands_string:
        r, c = find_element_location(board, size, box_symbol)

        # UP
        if command.upper() == m_up and r > 0:
            board[r][c], board[r - 1][c] = board[r - 1][c], board[r][c]

        # DOWN
        elif command.upper() == m_down and r < size - 1:
            board[r][c], board[r + 1][c] = board[r + 1][c], board[r][c]

        # LEFT
        elif command.upper() == m_left and c > 0:
            board[r][c], board[r][c - 1] = board[r][c - 1], board[r][c]

        # RIGHT
        elif command.upper() == m_right and c < size - 1:
            board[r][c], board[r][c + 1] = board[r][c + 1], board[r][c]

        # If puzzle is solved between action stop reading the command line
        if is_puzzle_solved(board):
            break

    return board

#TODO Class Board
# Check if the puzzle is in ordered state / if is solved
def is_puzzle_solved(board):
    flattened_board = flattened_matrix_in_list(board)
    result = all(
        [True if flattened_board[index] == index + 1 else False for index in range(len(flattened_board) - 1)])
    return result


# Receive element and search for his ROW and COL in the puzzle/matrix . Return tuple (r,c)
def find_element_location(board, size, number):
    return [(r, c) for c in range(size) for r in range(size) if board[r][c] == number][0]


def flattened_matrix_in_list(matrix):
    flattened_matrix = [item for row in matrix for item in row]
    return flattened_matrix


# -----------------------------------------------------MAIN-------------------------------------------------------------
if __name__ == '__main__':
    # Can be made with input and custom symbol
    empty_box_symbol = ' □'

    # Can be made with input and custom keys
    move_left, move_right, move_up, move_down = ('A', 'D', 'W', 'S')

    # Puzzle size can be any size. Recommended size is 3-10 for good visualisation
    while True:
        puzzle_size = input("Select Puzzle Size [3-10] ?")
        if puzzle_size.isdigit() and puzzle_size != "0":
            puzzle_size = int(puzzle_size)
            break

    assistant = SolverAssistant(empty_box_symbol, move_left, move_right, move_up, move_down)

    while True:

        #TODO Class Board

        # Create the puzzle board ( matrix )
        puzzle_board = create_puzzle(puzzle_size, empty_box_symbol)

        # Repeat u  ntil the puzzle is solved
        while not is_puzzle_solved(puzzle_board):

            # Prints for terminal Board and Control
            printing_the_board(puzzle_board, puzzle_size)
            printing_user_control(move_left, move_right, move_up, move_down)

            # User inputs are Directions in STRING 1 or Many , H - For assist , P - One piece help , F - Full solve
            command_input = input("Key + Enter -> :")

            if command_input.upper() == "H":
                assistant.hint_assist(puzzle_board, puzzle_size)

            elif command_input.upper() == "P":
                command_input = assistant.arrange_one_number_assist(deepcopy(puzzle_board), puzzle_size)

            elif command_input.upper() == "F":
                command_input = assistant.arrange_all_number_assist(deepcopy(puzzle_board), puzzle_size)  # Q?

            # input/assist command execution on board
            puzzle_board = move_the_empty_box(move_left, move_right, move_up, move_down,
                                              puzzle_board, puzzle_size, empty_box_symbol, command_input)

        # If the loop check for SOLVED board is True - Print final text
        print('\n\n-----------YOU WIN-----------')
        printing_the_board(puzzle_board, puzzle_size)

        # Loop for new game
        if not new_game():
            print("END GAME")
            break
