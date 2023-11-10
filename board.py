from random import randint


class Board:
    EMPTY_BOX_SYMBOL = ' □'

    def __init__(self, size):
        self.size = size
        self.puzzle_board = self.create_puzzle()

    # TODO maybe numbers can be str ? to fix the error highlighter
    # Create the puzzle based on size and arrange it in matrix. Return SOLVABLE version of the puzzle.
    def create_puzzle(self):
        while True:
            puzzle_generated = [number for number in range(self.size ** 2)]
            puzzle_generated[0] = self.EMPTY_BOX_SYMBOL
            puzzle_generated = [[puzzle_generated.pop(
                randint(0, len(puzzle_generated) - 1)) for _ in range(self.size)] for _ in range(self.size)]

            # If RANDOM puzzle is not solvable create NEW
            if self.check_if_puzzle_is_solvable(puzzle_generated):
                break

        return puzzle_generated

    # TODO Description
    def check_if_puzzle_is_solvable(self, puzzle_generated):
        flat_matrix = self.flattened_matrix_in_list(puzzle_generated)
        number_of_inversions = 0
        box_row, box_col = self.find_element_location(puzzle_generated, self.EMPTY_BOX_SYMBOL)

        # Going and compare all numbers in the array for Any Pair where A is before B. If A > B Inversions + 1!
        for a_numb_index in range((self.size ** 2) - 1):
            a_numb = flat_matrix[a_numb_index]

            for b_numb_index in range(a_numb_index + 1, self.size ** 2):
                b_numb = flat_matrix[b_numb_index]

                if type(a_numb) is type(b_numb):
                    if a_numb > b_numb:
                        number_of_inversions += 1

        # N(size) is ODD
        if self.size % 2 == 1:

            # SOLVABLE if Inversion is ODD
            if number_of_inversions % 2 == 0:
                return True

            # Every other combination is not solvable !
            else:
                return False

        # N(size) is EVEN.
        elif self.size % 2 == 0:

            # SOLVABLE if Inversion is EVEN and Empty box os on ODD row (count from bottom)
            if box_row % 2 == 1 and number_of_inversions % 2 == 0:
                return True

            # SOLVABLE if Inversion is ODD and Empty box os on EVEN row (count from bottom)
            elif box_row % 2 == 0 and number_of_inversions % 2 == 1:
                return True

            # Every other combination is not solvable !
            else:
                return False

    # TODO description maybe must be static and search in MATRIX

    @staticmethod
    def flattened_matrix_in_list(matrix):
        flattened_matrix = [item for row in matrix for item in row]
        return flattened_matrix

    # TODO description
    # Receive element and search for his ROW and COL in the puzzle/matrix . Return tuple (r,c)
    def find_element_location(self, matrix, number):
        return [(r, c) for c in range(self.size) for r in range(self.size) if matrix[r][c] == number][0]

    # Check if the puzzle is in ordered state / if is solved
    def is_puzzle_solved(self):
        flattened_board = self.flattened_matrix_in_list(self.puzzle_board)
        result = all(
            [True if flattened_board[index] == index + 1 else False for index in range(len(flattened_board) - 1)])
        return result

    # Receiving command string and move the empty box in the needed directions.
    def move_the_empty_box(self, m_left, m_right, m_up, m_down, commands_string):

        for command in commands_string:

            r, c = self.find_element_location(self.puzzle_board, self.EMPTY_BOX_SYMBOL)

            # UP
            if command.upper() == m_up and r > 0:
                self.puzzle_board[r][c], self.puzzle_board[r - 1][c] = self.puzzle_board[r - 1][c], \
                self.puzzle_board[r][c]

            # DOWN
            elif command.upper() == m_down and r < self.size - 1:
                self.puzzle_board[r][c], self.puzzle_board[r + 1][c] = self.puzzle_board[r + 1][c], \
                self.puzzle_board[r][c]

            # LEFT
            elif command.upper() == m_left and c > 0:
                self.puzzle_board[r][c], self.puzzle_board[r][c - 1] = self.puzzle_board[r][c - 1], \
                self.puzzle_board[r][c]

            # RIGHT
            elif command.upper() == m_right and c < self.size - 1:
                self.puzzle_board[r][c], self.puzzle_board[r][c + 1] = self.puzzle_board[r][c + 1], \
                self.puzzle_board[r][c]

            # If puzzle is solved between action stop reading the command line
            if self.is_puzzle_solved():
                break
