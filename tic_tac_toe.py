
def print_game_board(matrix_board):
    """
    Function prints game board on the model of matrix board 4x4
    :param matrix_board: matrix 4x4
    :return:
    prints matrix board in game
    """

    for row in range(len(matrix_board)):
        print()
        for col in range(len(matrix_board[row])):
            if 1 <= row <= 4 and 1 <= col <= 2:
                print(matrix_board[row][col], end=' | ')
            else:
                print(matrix_board[row][col], end=' ')
    print()


def create_matrix_board_3x3(matrix_board):
    """
    Function create matrix board 3x3 from matrix board 4x4 by removing first row and column
    :param matrix_board: matrix 4x4
    :return: matrix 3x3
    """
    new_matrix = [row[1:] for row in matrix_board[1:]]
    return new_matrix


def same_elements_in_row(matrix):
    """
    Function checks is row has the sme elements
    :param matrix: matrix 3x3
    :return: list (number of row, True or False, first element in row)
    """
    list_of_true_false = []
    for row in range(3):
        list_of_true_false.append((row, all(x == matrix[row][0] for x in matrix[row]), matrix[row][0]))
    return list_of_true_false


def change_rows_to_col(matrix):
    """
    Function changes rows to columns in matrix 3x3
    :param matrix: matrix 3x3
    :return: matrix 3x3
    """

    matrix_rows_to_col = []
    for row in range(3):
        matrix_rows_to_col_row = []
        for col in range(3):
            matrix_rows_to_col_row.append(matrix[col][row])
        matrix_rows_to_col.append(matrix_rows_to_col_row)
    return matrix_rows_to_col


def same_elements_in_col(matrix):
    """
    Function checks if in column of matrix are the same elements
    :param matrix: matrix 3x3
    :return: list (number of column, True or False, first element in row)
    """
    matrix_change = change_rows_to_col(matrix)
    return same_elements_in_row(matrix_change)


def same_elements_in_diagonal(matrix):
    """
    Function checks if in main diagonal or in antidiagonal the elements are the same
    :param matrix: matrix 3x3
    :return: list (number of row, True or False, element in diagonal)
    """
    list_true_false_main_diag = []
    list_true_false_anti_diag = []

    for row in range(3):
        list_true_false_main_diag.append((row, all(x == matrix[0][0] for x in matrix[row][row]), matrix[row][row]))
        list_true_false_anti_diag.append(
            (row, all(x == matrix[2][0] for x in matrix[row][3 - 1 - row]), matrix[row][3 - 1 - row]))

    main_true_false = []
    anti_true_false = []
    for element in range(3):
        main_true_false.append(list_true_false_main_diag[element][1])
        anti_true_false.append(list_true_false_anti_diag[element][1])

    if len(set(main_true_false)) == 1:
        return list_true_false_main_diag
    elif len(set(anti_true_false)) == 1:
        return list_true_false_anti_diag
    else:
        return [(0, False, '.'), (0, False, '.'), (0, False, '.')]


def who_wins_row_col(list_of_true_false):
    """
    Function returns element, that won the game
    :param list_of_true_false:
    :return: string 'X' or 'O'
    """
    for element in list_of_true_false:
        if element[1] is True:
            if element[2] != '.':
                return element[2]


def play_again():
    question = input('Do You want to play again? y/n ')
    if question.lower() == 'y':
        main()
    else:
        exit()


def main():
    matrix_board = [
        [' ', 'A ', ' B ', ' C'],
        [1, '.', '.', '.', ],
        [2, '.', '.', '.', ],
        [3, '.', '.', '.', ]
    ]

    dict_row = {'A': 1, 'B': 2, 'C': 3}

    print('Print game board')
    print_game_board(matrix_board)
    print()
    matrix_board_3x3 = create_matrix_board_3x3(matrix_board)

    turn = 'X'

    matrix_board_3x3_flatten = [el for row in matrix_board_3x3 for el in row]
    while '.' in matrix_board_3x3_flatten:
        print()

        try:
            move = input(f'Player {turn} mark position: ').title()

            if matrix_board[int(move[1])][dict_row[move[0]]] != '.':
                print('Put the mark on the other position.')
            else:
                matrix_board[int(move[1])][dict_row[move[0]]] = turn
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                print('print_game_board: ')
                print_game_board(matrix_board)
                matrix_board_3x3 = create_matrix_board_3x3(matrix_board)
                print(matrix_board_3x3)
                same_el_rows = same_elements_in_row(matrix_board_3x3)
                same_el_col = same_elements_in_col(matrix_board_3x3)
                same_el_diag = same_elements_in_diagonal(matrix_board_3x3)

                if who_wins_row_col(same_el_rows) is not None:
                    print('And the winner is:', who_wins_row_col(same_el_rows))
                    break
                elif who_wins_row_col(same_el_col) is not None:
                    print('And the winner is:', who_wins_row_col(same_el_col))
                    break
                elif who_wins_row_col(same_el_diag) is not None:
                    print('And the winner is:', who_wins_row_col(same_el_diag))
                    break
        except (ValueError, KeyError, IndexError) as e:
            print("Only combination of 'A', 'B', 'C' and 1, 2, 3, for example 'A1' is acceptable")

    play_again()


if __name__ == '__main__':
    main()
