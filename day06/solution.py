def part_1():
    """
    columns that need to be either added or multiplied, sum all those results.
    """
    total = 0
    # with open('day06/sample.txt', 'r') as _:
    with open('day06/input.txt', 'r') as _:
        number_matrix = []
        instruction = []
        for line in _:
            row = line.rstrip('\n')
            row = row.split()
            cleaned = []
            for i in row:
                if i in {'*', '+'}:
                    instruction.append(i)
                else:
                    cleaned.append(int(i))
            if cleaned:
                number_matrix.append(cleaned)

        for i in range(len(instruction)):
            op = instruction[i]
            if op == '+':
                for j in range(len(number_matrix)):
                    total += number_matrix[j][i]
            elif op == '*':
                product = 1
                for j in range(len(number_matrix)):
                    product *= number_matrix[j][i]
                total += product
        return total



def part_2():
    """
    the numbers are red right-to-left but also top-to-bottom.
    the spaces aren't distributed evenly, the numbers in cols aren't R or L aligned.
    need to take spaces into account then construct an int top to bottom.
    use op to denote new col
    """
    total = 0
    # with open('day06/sample.txt', 'r') as _:
    with open('day06/input.txt', 'r') as _:
        number_matrix = []
        instruction = []
        for line in _:
            with_spaces = []
            row = line.rstrip('\n')
            for i in row:
                with_spaces.append(i)
            if with_spaces[0] in {'*', '+'}:
                instruction = with_spaces
            else:
                number_matrix.append(with_spaces)

        cursor = 0
        while cursor < len(instruction):
            op = instruction[cursor]
            neighbor_distance = 1
            if op == '*' and cursor == len(instruction) - 1:
                # final instruction needs different handling
                neighbor_distance = 2  # input
                # neighbor_distance = 3  # sample
            else:
                while instruction[cursor + neighbor_distance] == ' ':
                    neighbor_distance += 1

            rearranged = ''
            for c in range(neighbor_distance):
                for r in number_matrix:
                    rearranged = rearranged + r[cursor+c]
                rearranged = rearranged + ' '
            rearranged = rearranged.split()

            if op == '+':
                for num in rearranged:
                    total += int(num)
            else:
                product = 1
                for num in rearranged:
                    product *= int(num)
                total += product

            cursor += neighbor_distance

        return total


if __name__ == '__main__':
    # filenames are hardcoded in func
    # run with python day06/solution.py
    # print(part_1())
    print(part_2())
