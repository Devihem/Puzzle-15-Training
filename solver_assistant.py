import puzzle_15_custom


class SolverAssistant:
    def __init__(self, box_symbol, left, right, up, down):
        self.empty_box_symbol = box_symbol
        self.m_left = left
        self.m_right = right
        self.m_up = up
        self.m_down = down

    # Assistant Print Help Information
    def hint_assist(self, board, size):

        # Find all needed positions of Correct Number Place , Current Number Place , Empty Box
        number_box, go_r, go_c, num_r, num_c, box_r, box_c = self.grouped_elements_searching(board, size)

        print("\n\n\n\n You are here:", box_r + 1, box_c + 1)
        print(" First misplaced number is", number_box, " And is Here:", num_r + 1, num_c + 1)
        print(" You must move it Here:", go_r + 1, go_c + 1)
        return

    # Move Empty box go over the target number
    def move_positioning_zone_1_2_3(self, size, num_r, num_c, box_r, box_c, command_line):

        # for any row from 1 to n-1
        if num_r < size - 1:
            command_line += (box_c - num_c) * self.m_left + (box_r - num_r) * self.m_up
            num_r += 1

        # if the number is on the last row == size/n
        elif num_r == size - 1:
            command_line += self.m_up + (box_c - num_c) * self.m_left

        return num_r, command_line

    # Move Target box to the column he must be placed
    def move_left_or_right_zone_1_2_3(self, go_c, num_c, command_line):

        # Move it to LEFT
        if go_c < num_c:
            command_line += (num_c - go_c) * (self.m_left + self.m_down + self.m_right + self.m_up + self.m_left)

        # Move it to RIGHT
        elif num_c < go_c:
            command_line += (go_c - num_c) * (self.m_right + self.m_down + self.m_left + self.m_up + self.m_right)

        return command_line

    # Move Target Box to the row he must be placed
    def move_go_up_from_right_zone_1(self, num_r, go_r, command_line):
        command_line += (num_r - go_r - 1) * (
                self.m_down + self.m_right + self.m_up + self.m_up + self.m_left) + self.m_down

        return command_line

    # Move Target Number to the corner position he must be placed + Pattern Corner Right Vertical
    def move_stack_corner_right_zone_2(self, num_r, go_r, command_line):
        command_line += ((num_r - go_r - 2) * (self.m_down + self.m_left + self.m_up + self.m_up + self.m_right) +
                         self.pattern_move_right_corner_stack())
        return command_line

    # Move Target Number to the corner position he must be placed + Pattern Corner Left Horizontal
    def move_stack_corner_left_zone_3(self, num_c, go_c, command_line):
        command_line += ((num_c - (go_c + 1)) * (self.m_left + self.m_down + self.m_right + self.m_up + self.m_left) +
                         self.pattern_horiz_left_corner_stack())
        return command_line

    # Move Pattern ( rotate current and last target number to fit in corner ) "WASDS-AWWDS"
    def pattern_move_right_corner_stack(self):
        return (self.m_up + self.m_left + self.m_down + self.m_right + self.m_down +
                self.m_left + self.m_up + self.m_up + self.m_right + self.m_down)

    # Move Pattern ( rotate current and last target number to fit in corner ) "SDWAASD-WDSAAWD"

    def pattern_horiz_left_corner_stack(self):
        return (self.m_down + self.m_right + self.m_up + self.m_left + self.m_left + self.m_down + self.m_right +
                self.m_up + self.m_right + self.m_down + self.m_left + self.m_left + self.m_up + self.m_right)

    def arrange_one_number_assist(self, board, size):

        # All pattern command are added in this string
        command_line = ''

        # Starting Position Pattern - go to bottom of the puzzle [MAX_ROW: MAX_COL]
        board, command_line = self.move_to_start_position(board, size)
        if puzzle_15_custom.is_puzzle_solved(board):
            return command_line

        # Find missing number and all needed positions of Correct Number Place , Current Number Place , Empty Box Place
        number_box, go_r, go_c, num_r, num_c, box_r, box_c = self.grouped_elements_searching(board, size)

        # Zone - 1: [GO_ROWS < MAX_ROWS - 2 and GO_COL < MAX_COL -1 ] elements that must be placed in these dimension.
        if (go_r < (size - 2)) and (go_c < (size - 1)):

            # move 1 - go OVER the number
            num_r, command_line = self.move_positioning_zone_1_2_3(size, num_r, num_c, box_r, box_c, command_line)

            # move 2 - move the number LEFT or RIGHT to the same column
            command_line = self.move_left_or_right_zone_1_2_3(go_c, num_c, command_line)

            # move 3 - move the number UP to the same row
            command_line = self.move_go_up_from_right_zone_1(num_r, go_r, command_line)

            return command_line

        # Zone - 2 [GO_ROWS < MAX_ROWS - 2 and MAX_COL = GO_COL ] pattern for elements in these dimensions.
        elif (go_r < (size - 2)) and (go_c == (size - 1)):

            # move 1 - go OVER the number
            num_r, command_line = self.move_positioning_zone_1_2_3(size, num_r, num_c, box_r, box_c, command_line)

            # move 2 - move the number LEFT or RIGHT to the same column
            command_line = self.move_left_or_right_zone_1_2_3(go_c, num_c, command_line)

            # move 3 - move the number in the up right corner
            command_line = self.move_stack_corner_right_zone_2(num_r, go_r, command_line)

            return command_line

        # Zone - 3 [GO_ROWS >= MAX_ROWS - 1 and GO_COL <= MAX_COL -2 ] pattern for elements in these dimensions.
        elif (go_r >= (size - 2)) and (go_c <= (size - 3)):

            # move 1 - go OVER the number
            num_r, command_line = self.move_positioning_zone_1_2_3(size, num_r, num_c, box_r, box_c, command_line)

            # move 2 - move the number LEFT to the same column and row
            if go_r == size - 1:
                command_line = self.move_left_or_right_zone_1_2_3(go_c, num_c, command_line)

            # move 3 - # For numbers in upper ROW ( Zone 3 corner) move the number in the corner
            elif go_r == size - 2:
                command_line = self.move_stack_corner_left_zone_3(num_c, go_c, command_line)

            return command_line

        # Zone 4 - When only 4 blocks are left:
        elif (go_r >= (size - 2)) and (go_c >= (size - 2)):

            if num_r == (size - 1):
                command_line += "WASD"

            else:
                command_line += "AWDS"

            return command_line

    # Use the method (arrange_one_number_assist) to order all numbers
    def arrange_all_number_assist(self, board, size):
        total_command_line = ''

        while not puzzle_15_custom.is_puzzle_solved(board):
            command_line = self.arrange_one_number_assist(board, size)

            board = puzzle_15_custom.move_the_empty_box(self.m_left, self.m_right, self.m_up, self.m_down, board, size,
                                                        self.empty_box_symbol, command_line)
            total_command_line += command_line
        return total_command_line

    # ------------------------------------------------HELPERS----------------------------------------------------------
    def move_to_start_position(self, board, size):
        box_r, box_c = self.find_num_box_current_loc(board, size, self.empty_box_symbol)

        command_string = ((size - 1 - box_c) * self.m_right) + (((size - 1) - box_r) * self.m_down)

        board = puzzle_15_custom.move_the_empty_box(self.m_left, self.m_right, self.m_up, self.m_down,
                                                    board, size, self.empty_box_symbol, command_string)
        return board, command_string

    def grouped_elements_searching(self, board, size):
        number_box = self.find_first_missing_number_box(board, size)
        go_r, go_c = self.find_number_place_loc(size, number_box)
        num_r, num_c = self.find_num_box_current_loc(board, size, number_box)
        box_r, box_c = self.find_num_box_current_loc(board, size, self.empty_box_symbol)

        return number_box, go_r, go_c, num_r, num_c, box_r, box_c

    @staticmethod
    def find_first_missing_number_box(board, size):
        flat_matrix_list = puzzle_15_custom.flattened_matrix_in_list(board)
        for num_flat_index in range(size ** 2 - 1):
            # 8 <= index  < 12:
            if (size ** 2 - size * 2) <= num_flat_index < (size ** 2 - size):
                if (num_flat_index + 1 + size) != flat_matrix_list[num_flat_index + size]:
                    number_box = num_flat_index + 1 + size
                    return number_box

                elif num_flat_index + 1 != flat_matrix_list[num_flat_index]:
                    number_box = num_flat_index + 1
                    return number_box

            elif num_flat_index + 1 != flat_matrix_list[num_flat_index]:
                number_box = num_flat_index + 1
                return number_box

    @staticmethod
    def find_num_box_current_loc(board, size, number_box):
        el_r, el_c = puzzle_15_custom.find_element_location(board, size, number_box)
        return el_r, el_c

    @staticmethod
    def find_number_place_loc(size, number_box):
        go_r, go_c = ((number_box - 1) // size, ((number_box - 1) % size))
        return go_r, go_c
