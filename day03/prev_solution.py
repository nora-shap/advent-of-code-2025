def part_1():
    """
    labeled with joltage 1-9
    arranged in banks, each line is a bank, you cannot rearrange
    select 2 per bank
    the joltage that the bank produces is equal to the number formed by the digits on the batteries you've selected
    find the largest possible joltage that each bank can produce
    total output joltage is the sum of the maximum joltage from each bank
    """
    total = 0
    with open('day03/input.txt', 'r') as banks:
        for bank in banks:
            bank = bank.rstrip()
            first = max(bank[:-1])
            first_i = bank.index(first)
            second = max(bank[first_i + 1:])
            total += int(f'{first}{second}')
    return total


def part_2():
    """
    make the largest joltage by selecting 12 within each bank
    still cannot reorder but the 12 don't need to be sequential
    """
    total = 0
    with open('day03/input.txt', 'r') as banks:
        for bank in banks:
            bank = bank.rstrip()
            b = -11
            selections = []
            for x in range(12):
                if x == 11:
                    sli = bank
                else:
                    sli = bank[:b]
                n = max(sli)
                selections.append(n)
                a = sli.index(n) + 1
                bank = bank[a:]
                b += 1

            total += int(''.join(selections))

    return total


if __name__ == '__main__':
    # filenames are hardcoded in func
    print(part_1())
    print(part_2())