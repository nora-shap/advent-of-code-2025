import csv

def get_ranges():
    # with open('day02/sample.txt', 'r') as id_ranges:
    with open('day02/input.txt', 'r') as id_ranges:
        reader_obj = csv.reader(id_ranges)
        return next(reader_obj)


def part_1():
    """
    invalid product ids added to db. check ranges
    Invalid ID = made only of some sequence of digits repeated TWICE
    find all of the invalid IDs that appear in the given ranges, sum them.
    """
    ranges = get_ranges()
    total = 0

    for range_as_str in ranges:
        x = range_as_str.split('-')
        start = int(x[0])
        end = int(x[-1])
        for i in range(start, end+1):
            as_str = str(i)
            if len(as_str) % 2 == 0:
                first_half = as_str[0:len(as_str)//2]
                second_half = as_str[len(as_str)//2:]
                if first_half == second_half:
                    total += i

    return total



def part_2():
    """
    invalid if it is made only of some sequence of digits repeated at least twice
    """
    ranges = get_ranges()
    total = 0

    for range_as_str in ranges:
        x = range_as_str.split('-')
        start = int(x[0])
        end = int(x[-1])
        for i in range(start, end + 1):
            as_str = str(i)
            num_digits_in_sequence = len(as_str)
            max_sequence_len = num_digits_in_sequence // 2
            sequence_len = max_sequence_len
            while sequence_len > 0:
                if num_digits_in_sequence % sequence_len == 0:
                    num_sequences = num_digits_in_sequence // sequence_len
                    sequences = set()
                    s = 0
                    for z in range(num_sequences):
                        sequences.add(as_str[s:s+sequence_len])
                        s += sequence_len
                    if len(sequences) == 1:
                        total += i
                        break  # multiple matches in the same i don't count, so if you find one, don't keep searching this i
                sequence_len -= 1


    return total


if __name__ == '__main__':
    # filenames are hardcoded in func
    # run with python day02/solution.py
    print(part_1())
    print(part_2())