def part_1():
    """
    It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs.
    The fresh ID ranges are inclusive
    The ranges can also overlap; an ingredient ID is fresh if it is in any range
    which of the available ingredient IDs are fresh?
    2 data sets: int ranges (inclusive, overlapping), int list
    return count of ints in both lists
    """
    fresh_and_in_stock = set()
    list_of_lists = []
    blank_line = False
    # with open('day05/sample.txt', 'r') as _:
    with open('day05/input.txt', 'r') as _:
        for line in _:
            line = line.rstrip('\n')
            if line == '':
                blank_line = True
                continue

        # list of ranges. for each in stock, if between the two, count it and break
        # keep the ranges in order so can quit when no more matches
            if not blank_line:
                input = line.split('-')
                start = int(input[0])
                end = int(input[1])
                this_range = [start, end]
                list_of_lists.append(this_range)

            if blank_line:
                current_id = int(line)
                for r in list_of_lists:
                    if current_id >= r[0] and current_id <= r[1]:
                        fresh_and_in_stock.add(current_id)

    return len(fresh_and_in_stock)


def part_2():
    """
    now it's ranges only.
    how many (unique) ints are in the ranges
    """
    total = 0
    list_of_lists = []
    # with open('day05/sample.txt', 'r') as _:
    with open('day05/input.txt', 'r') as _:
        for line in _:
            line = line.rstrip('\n')
            if line == '':
                break

            input = line.split('-')
            start = int(input[0])
            end = int(input[1])
            this_range = [start, end]
            list_of_lists.append(this_range)

        ordered_list = sorted(list_of_lists, key=lambda x: (x[0], x[1]))
        n_changed = 1
        while n_changed != 0:
            n_changed = 0
            merged_list = []
            for i in range(len(ordered_list)):
                if i == 0:
                    continue

                prev_range = ordered_list[i-1]
                curr_range = ordered_list[i]
                if prev_range == curr_range:
                    continue
                elif prev_range[1] + 1 == curr_range[0]:
                    merged = [min([prev_range[0], curr_range[0]]), max([prev_range[1], curr_range[1]])]
                    merged_list.append(merged)
                    n_changed += 1
                    was_merged = True
                elif prev_range[1] < curr_range[0]:
                    merged_list.append(prev_range)
                    was_merged = False
                else:
                    merged = [min([prev_range[0], curr_range[0]]), max([prev_range[1], curr_range[1]])]
                    merged_list.append(merged)
                    n_changed += 1
                    was_merged = True

                if i + 1 == len(ordered_list) and not was_merged:
                    merged_list.append(curr_range)
                if was_merged:
                    ordered_list[i] = merged

            ordered_list = merged_list

        # now I have optimized ranges, get inclusive difference in range
        for r in ordered_list:
            inclusive_diff = r[1] - r[0] + 1
            total += inclusive_diff
    return total


if __name__ == '__main__':
    # filenames are hardcoded in func
    # run with python day05/solution.py
    # print(part_1())
    print(part_2())



