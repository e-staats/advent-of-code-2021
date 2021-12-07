from rich import print
from icecream import ic


def main():
    danger_dict = {}
    danger_count = 0
    with open("../inputs/day5.txt", "r") as file:
        reading = True
        while reading == True:
            line_def = file.readline().rstrip().split(" ")
            if line_def == [""]:
                reading == False
                break
            start = list(map(int, line_def[0].split(",")))
            end = list(map(int, line_def[2].split(",")))
            if start[0] == end[0]:
                danger_count += add_danger_count(start, end, 1, danger_dict)
            elif start[1] == end[1]:
                danger_count += add_danger_count(start, end, 0, danger_dict)
            else:
                danger_count += add_down_diagonal_danger_count(start, end, danger_dict)
    print(danger_count)


def add_danger_count(start, end, direction, dictionary):
    danger_count = 0
    starting_point = min(start[direction], end[direction])
    ending_point = max(start[direction], end[direction])
    constant = start[1 - direction]
    for i in range(starting_point, ending_point + 1, 1):
        coord = [0, 0]
        coord[direction] = i
        coord[1 - direction] = constant
        danger_count += cache_intersections(coord, dictionary)
    return danger_count


def add_down_diagonal_danger_count(start, end, dictionary):
    danger_count = 0
    inc_x, inc_y = (
        int((end[0] - start[0]) / abs(end[0] - start[0])),
        int((end[1] - start[1]) / abs(end[1] - start[1])),
    )
    coord = [start[0], start[1]]
    for i in range(abs(end[0] - start[0]) + 1):
        danger_count += cache_intersections(coord, dictionary)
        coord[0] += inc_x
        coord[1] += inc_y
    return danger_count


def cache_intersections(coord, dictionary):
    coord = ",".join(str(item) for item in coord)
    inc = 0
    if coord in dictionary.keys():
        if dictionary[coord] == 1:
            inc = 1
        dictionary[coord] += 1
    else:
        dictionary[coord] = 1
    return inc


if __name__ == "__main__":
    main()
