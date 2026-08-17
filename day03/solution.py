def part_1():
    """
    need to power the escalator with batteries
    each battery has a joltage 0-9, arranged in banks
    row of integers, select 2 ints from each row to make the largest int, sum them
    no rearranging
    """
    total = 0
    # with open('day03/sample.txt', 'r') as _:
    with open('day03/input.txt', 'r') as _:
        for battery_bank in _:
            batteries = list(battery_bank.rstrip('\n'))
            # find largest number in str, don't look at -1
            tens_options = batteries[:-1]
            tens = max(tens_options)
            tens_i = tens_options.index(tens)
            tens = int(tens) * 10
            # find largest number to the right of first number
            ones_options = list(battery_bank)[tens_i + 1:]
            ones = max(ones_options)

            max_int = tens + int(ones)
            total += max_int
    return total


def part_2():
    """
    row of integers, select 12 ints from each row to make the largest int, sum them
    no rearranging but you can skip
    """
    total = 0
    # with open('day03/sample.txt', 'r') as _:
    with open('day03/input.txt', 'r') as _:
        for battery_bank in _:
            joltage = []
            batteries = list(battery_bank.rstrip('\n'))
            start_i = 0
            end_i = 11
            for x in range(end_i + 1):
                if end_i == 0:
                    options = batteries[start_i:]
                else:
                    options = batteries[start_i:-end_i]
                selection = max(options)
                selection_i = options.index(selection) + start_i
                batteries.pop(selection_i)
                joltage.append(selection)
                start_i = selection_i
                end_i -= 1

            max_int = int(''.join(joltage))
            total += max_int
    return total


if __name__ == '__main__':
    # filenames are hardcoded in func
    # run with python day03/solution.py
    print(part_1())
    print(part_2())
