from collections import defaultdict


def part_1():
    """
    input is a tachyon manifold
    beam enters at S, first row is all '.' with 1 'S'
    empty space `.`, splitter `^`
    when you encounter a splitter it splits the beam
    beams can merge if split side-by-side
    last line is all '.'
    splitter always has space arount it, never [0] or [-1]
    count number of times a beam hits a splitter
    """
    count = 0
    # with open('day07/sample.txt', 'r') as _:
    with open('day07/input.txt', 'r') as _:
        first_line = True
        starting_beam_indices = set()
        for line in _:
            line = line.rstrip('\n')
            if first_line:
                starting_position = line.index('S')
                starting_beam_indices = {starting_position}
                first_line = False
            else:
                splitter_i = line.find('^')
                beam_indices = set()
                while splitter_i >= 0:
                    if splitter_i in starting_beam_indices:
                        beam_indices.add(splitter_i - 1)
                        beam_indices.add(splitter_i + 1)
                        starting_beam_indices.remove(splitter_i)
                        count +=1
                    splitter_i = line.find('^', splitter_i + 1)
                starting_beam_indices = starting_beam_indices | beam_indices

    return count


def part_2():
    """
    single particle beam
    timeline splits each time it hits a splitter
    number of timelines after 1 particle completes all possible journeys
    """
    # lines = open('day07/sample.txt').read().splitlines()
    lines = open('day07/input.txt').read().splitlines()

    beams = defaultdict(int)

    # get starting position
    first_line = lines[0]
    starting_position = first_line.index('S')
    beams[starting_position] = 1

    for line in lines[::2]:  # can skip every other line
        for i in set(beams.keys()):
            # dict keys are all the positions that have a beam right now
            # need to compare that to the contents of the current line
            if line[i] == "^":
                # if there is a beam that hits a splitter in this pos
                # all timelines at this pos split, assign to either side
                beams[i - 1] += beams[i]
                beams[i + 1] += beams[i]
                # remove the original beam count as it has been split
                del beams[i]

    return sum(beams.values())

if __name__ == '__main__':
    # filenames are hardcoded in func
    # run with python day07/solution.py
    # print(part_1())
    print(part_2())
