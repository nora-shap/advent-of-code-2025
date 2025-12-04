def make_circular(pointing_at):
    if pointing_at < 0:
        pointing_at = 100 + pointing_at
    if pointing_at > 99:
        pointing_at = pointing_at - 100
    return pointing_at

def part_1():
    count = 0
    pointing_at = 50

    with open('day01/part_1_input.txt', 'r') as instructions:
        for instruction in instructions:
            direction = instruction[0]
            amount = int(instruction[1:])
            if direction == 'L':
                amount *= -1
            pointing_at += amount

            # make circular
            while pointing_at < 0 or pointing_at > 99:
                pointing_at = make_circular(pointing_at)

            if pointing_at == 0:
                count += 1

    return count


def part_2():
    """count the number of times any click causes the dial to point at 0,
    regardless of whether it happens during a rotation or at the end of one.
    """
    count = 0
    passes = 0
    pointing_at = 50

    with open('day01/part_1_input.txt', 'r') as instructions:
        for instruction in instructions:
            started_at_0 = False
            if pointing_at == 0:
                started_at_0 = True

            direction = instruction[0]
            amount = int(instruction[1:])
            if direction == 'L':
                amount *= -1
            pointing_at += amount

            had_to_be_corrected = False
            while pointing_at < 0 or pointing_at > 99:
                had_to_be_corrected = True
                pointing_at = make_circular(pointing_at)
                passes += 1

            if had_to_be_corrected and pointing_at == 0 and direction == 'R':
                # ending on 0 from R direction incurs 1 extra pass
                passes += -1

            if had_to_be_corrected and started_at_0 and direction == 'L':
                # starting at 0 and moving L incurs 1 extra pass
                passes += -1

            if pointing_at == 0:
                count += 1

    return count + passes


if __name__ == '__main__':
    # filenames are hardcoded in func
    print(part_1())
    print(part_2())
