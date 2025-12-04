import csv

def gimmie_row():
    """
    input is just 1 line, gives us a list of str ranges
    """
    with open('day02/part_1_input.txt', 'r') as id_ranges:
        reader_obj = csv.reader(id_ranges)
        return next(reader_obj)

def part_1():
    """
    invalid product ids in input, identify them.
    input is ranges??? in csv,  format is first_id-last_id
    invalid id == made ONLY of some sequence of digits repeated TWICE
    none have leading 0's
    find all invalid ids that appear in the given range, start and end inclusive
    add the invalid ids together
    """
    row = gimmie_row()
    total = 0

    for id_range in row:
        split_ids = id_range.split('-')
        start = int(split_ids[0])
        end = int(split_ids[1])

        for id in range(start, end + 1):
            id_as_str = str(id)
            is_even = len(id_as_str) % 2 == 0
            if is_even:
                front, back = id_as_str[:len(id_as_str)//2], id_as_str[len(id_as_str)//2:]
                if front == back:
                    total += id

    return total


def part_2():
    """
    definition of invalid has changed:
    made ONLY of some sequence, repeated twice OR MORE
    """
    row = gimmie_row()
    total = 0

    for id_range in row:
        split_ids = id_range.split('-')
        start = int(split_ids[0])
        end = int(split_ids[1])

        for id in range(start, end + 1):
            id_as_str = str(id)
            for i in range(len(id_as_str)//2):
                sequence_to_check = id_as_str[:i + 1]
                if len(id_as_str) % (i + 1) == 0:
                    c = id_as_str.count(sequence_to_check)
                    if c > 1:
                        repeats = set()
                        slice_cut = 0
                        while slice_cut < len(id_as_str):
                            repeats.add(id_as_str[slice_cut:slice_cut+i+1])
                            slice_cut += i+1
                        if len(repeats) == 1:
                            total += id
                            break
    return total


if __name__ == '__main__':
    # filenames are hardcoded in func
    print(part_1())
    print(part_2())