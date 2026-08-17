def adjust(current):
    if current < 0:
        current += 100
    if current > 99:
        current -= 100
    return current


def part_1():
    """
    Need to get into a safe.
    safe dial: 0-99 in order with 1 hand
    input is a sequence of rotations, one per line, starts with L or R + distance
    dial starts at 50
    The actual password is the number of times the dial lands on 0
    """
    counter = 0
    start = 50
    with open('day01/input.txt', 'r') as _:
    # with open('day01/sample.txt', 'r') as _:
        for rotation in _:
            direction = rotation[0]
            distance = int(rotation[1:]) if direction == 'R' else int(rotation[1:]) * -1

            start += distance
            while start >= 100:
                start = adjust(start)
            while start <= -100:
                start = adjust(start)

            if start == 0:
                counter += 1

    return counter


def part_2():
    """
    Count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.
    passing 0 or landing on 0 += counter
    """
    counter = 0
    start = 50
    with open('day01/input.txt', 'r') as _:
    # with open('day01/sample.txt', 'r') as _:
        for rotation in _:
            direction = rotation[0]
            distance = int(rotation[1:]) if direction == 'R' else int(rotation[1:]) * -1

            current = start + distance
            was_adj = False
            while current > 99:
                current = adjust(current)
                was_adj = True
                counter += 1

            while current < 0:
                current = adjust(current)
                was_adj = True
                counter += 1


            if was_adj and current == 0 and direction == 'R':
                # ending on 0 from R direction incurs 1 extra count
                counter += -1

            if was_adj and start == 0 and direction == 'L':
                # starting at 0 and moving L incurs 1 extra count
                counter += -1

            if current == 0:
                counter += 1

            start = current

    return counter


if __name__ == '__main__':
    # filenames are hardcoded in func
    # run with python day01/solution.py
    print(part_1())
    print(part_2())
