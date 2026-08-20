from math import sqrt


def get_closest_neighbor(current_box, neighbors):
    current_box_formatted = current_box.split(',')
    distances = []
    for i in range(len(neighbors)):
        neighbor = neighbors[i].split(',')
        distance = round(sqrt((int(current_box_formatted[0]) - int(neighbor[0])) ** 2 + (int(current_box_formatted[1]) - int(neighbor[1])) ** 2 + (int(current_box_formatted[2]) - int(neighbor[2])) ** 2), 3)
        distances.append([distance, [current_box, neighbors[i]]])

    distances.sort(key=lambda c: c[0])
    return distances


def part_1():
    """
    junction boxes connected by strings of lights
    when to boxes are connected electricity can pass between them
    list of 3d positions
    1 line per box, x,y,z coordinates
    connect pairs of junction boxes that are as close together as possible according to straight-line distance
    connecting 2 boxes makes them a circuit. single boxes are also a circuit
    can connect multiple to one circuit.
    for sample, make 10 connections, sort by circuit with most boxes, multiply top 3
    for input, connect the 1000 closest pairs
    The 1000 closest ones must be connected. you need to connect them all - so electricity can reach every box
    """
    # input = 'sample'
    input = 'input'
    connection_count = 10 if input == 'sample' else 1000
    lines = open(f'day08/{input}.txt').read().splitlines()

    circuits = []
    distances = []

    for i in range(len(lines)):
        current_box = lines[i]
        sorted_distances = get_closest_neighbor(current_box, lines[:i] + lines[i + 1:])
        distances.extend(sorted_distances)

    distances.sort(key=lambda c: c[0])

    connections = 0
    for cnxn in distances[::2]:
        if connections < connection_count:
            added = -1
            for i in range(len(circuits)):
                c = circuits[i]
                if cnxn[1][0] in c and cnxn[1][1] in c:
                    connections += 1
                    added = i
                    break
                if cnxn[1][0] in c or cnxn[1][1] in c:
                    if added < 0:
                        c.add(cnxn[1][0])
                        c.add(cnxn[1][1])
                        added = i
                        connections+=1
                    else:
                        to_be_merged = c
                        merge_into = circuits[added]
                        merge_into = merge_into | to_be_merged
                        circuits[added] = merge_into
                        c.clear()

            if added < 0:
                circuits.append({cnxn[1][0], cnxn[1][1]})
                connections += 1

    circuits.sort(key=lambda c: len(c), reverse=True)
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def part_2():
    """
    keep connecting until in 1 circuit
    1 circuit means len(circuits) == 1 and len(circuits[0]) == len(lines)
    find the first connection which causes all of the junction boxes to form a single circuit, sum x coords
    """
    # input = 'sample'
    input = 'input'
    lines = open(f'day08/{input}.txt').read().splitlines()
    line_count = len(lines)

    circuits = [set()]
    distances = []

    for i in range(len(lines)):
        current_box = lines[i]
        sorted_distances = get_closest_neighbor(current_box, lines[:i] + lines[i + 1:])
        distances.extend(sorted_distances)

    distances.sort(key=lambda c: c[0])

    connections = 0
    for cnxn in distances[::2]:
        added = -1
        for i in range(len(circuits)):
            c = circuits[i]
            if cnxn[1][0] in c and cnxn[1][1] in c:
                connections += 1
                added = i
                break
            if cnxn[1][0] in c or cnxn[1][1] in c:
                if added < 0:
                    c.add(cnxn[1][0])
                    c.add(cnxn[1][1])
                    added = i
                    connections += 1
                else:
                    to_be_merged = c
                    merge_into = circuits[added]
                    merge_into = merge_into | to_be_merged
                    circuits[added] = merge_into
                    c.clear()

        if added < 0:
            circuits.append({cnxn[1][0], cnxn[1][1]})
            connections += 1
        circuits.sort(key=lambda c: len(c), reverse=True)
        if len(circuits[0]) == line_count:
            element_1 = cnxn[1][0].split(',')
            x1 = int(element_1[0])
            element_2 = cnxn[1][1].split(',')
            x2 = int(element_2[0])
            break

    return x1 * x2


if __name__ == '__main__':
    # filenames are hardcoded in func
    # run with python day08/solution.py
    # print(part_1())
    print(part_2())

