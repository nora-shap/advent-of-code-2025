def make_me_matrix():
    the_matrix = []
    # with open('day04/sample.txt', 'r') as _:
    with open('day04/input.txt', 'r') as _:
        for line in _:
            row = list(line.rstrip('\n'))
            the_matrix.append(row)
    return the_matrix


def get_surroundings(the_matrix, i, j, rows, cols):
    # current_position = (i, j)
    directions = [
        (0, 1),  # right
        (1, 1),  # right down
        (1, 0),  # down
        (1, -1),  # down left
        (0, -1),  # left
        (-1, -1),  # left up
        (-1, 0),  # up
        (-1, 1)  # right, up
    ]
    surroundings = []
    for x, y in directions:
        new_row, new_col = i + x, j + y
        if 0 <= new_row < rows and 0 <= new_col < cols:  # boundary check
            surroundings.append(the_matrix[new_row][new_col])
    return surroundings


def part_1():
    """
    a `@` is accessible if there are fewer than four `@` in the eight adjacent positions
    How many rolls of paper can be accessed?
    matrix with `.` and `@`
    for each `@`, how many have < 4 `@` around them
    """
    count = 0
    the_matrix = make_me_matrix()
    rows = len(the_matrix)
    cols = len(the_matrix[0])

    for i in range(rows):
        for j in range(cols):
            if the_matrix[i][j] == '@':
                # get the 8 surrounding cells
                surrounds = get_surroundings(the_matrix, i, j, rows, cols)
                n_nearby_rolls = surrounds.count('@')
                if n_nearby_rolls < 4:
                    count += 1

    return count



def part_2():
    """
    if it can be accessed it can be removed, which might change the math of the surrounding `@`
    do passes removing `@` if they can be accessed
    How many total can be removed
    """
    count = 0
    the_matrix = make_me_matrix()
    rows = len(the_matrix)
    cols = len(the_matrix[0])

    removed_this_pass = 1
    while removed_this_pass != 0:
        removed_this_pass = 0
        for i in range(rows):
            for j in range(cols):
                if the_matrix[i][j] == '@':
                    # get the 8 surrounding cells
                    surrounds = get_surroundings(the_matrix, i, j, rows, cols)
                    n_nearby_rolls = surrounds.count('@')
                    if n_nearby_rolls < 4:
                        count += 1
                        removed_this_pass += 1
                        the_matrix[i][j] = '.'

    return count

if __name__ == '__main__':
    # filenames are hardcoded in func
    # run with python day04/solution.py
    print(part_1())
    print(part_2())