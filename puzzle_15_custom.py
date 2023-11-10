# TODO this must be removed / fix dependencies /

from copy import deepcopy
from board import Board
from solver_assistant import SolverAssistant


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


# ----------------------------------------------------------------------------------------------------------------------
# Ask the user for new game, before quit
def new_game():
    while True:
        new_game_input = input("Do you want to play another game ? Y/N")
        if new_game_input.upper() == "Y":
            return True
        elif new_game_input.upper() == "N":
            return False


# -----------------------------------------------------MAIN-------------------------------------------------------------
if __name__ == '__main__':

    # TODO control.
    move_left, move_right, move_up, move_down = ('A', 'D', 'W', 'S')

    # Set the puzzle size. Recommended is 3-10 for better visualisation.
    while True:
        puzzle_size = input("Select Puzzle Size [3-10] ?")
        if puzzle_size.isdigit() and puzzle_size != "0":
            puzzle_size = int(puzzle_size)
            break

    while True:

        board = Board(puzzle_size)
        assistant = SolverAssistant(move_left, move_right, move_up, move_down, deepcopy(board))

        # Repeat until the puzzle is solved
        while not board.is_puzzle_solved():

            # Prints for terminal Board and Control
            printing_the_board(board.puzzle_board, puzzle_size)
            printing_user_control(move_left, move_right, move_up, move_down)

            # TODO better explanation
            # User inputs are Directions in STRING 1 or Many , H - For assist , P - One piece help , F - Full solve
            command_input = input("Key + Enter -> :")

            # TODO this 3 checks can be abstract
            if command_input.upper() == "H":
                assistant.clone_board.puzzle_board = deepcopy(board.puzzle_board)
                assistant.hint_assist()

            elif command_input.upper() == "P":
                assistant.clone_board.puzzle_board = deepcopy(board.puzzle_board)
                command_input = assistant.arrange_one_number_assist()

            elif command_input.upper() == "F":
                assistant.clone_board.puzzle_board = deepcopy(board.puzzle_board)
                command_input = assistant.arrange_all_number_assist()

            # input/assist command execution on board
            board.move_the_empty_box(move_left, move_right, move_up, move_down, command_input)

        # If the loop check for SOLVED board is True - Print final text
        print('\n\n-----------YOU WIN-----------')
        printing_the_board(board.puzzle_board, puzzle_size)

        # Loop for new game
        if not new_game():
            print("END GAME")
            break
