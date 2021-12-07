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
    print(danger_count)


def add_danger_count(start, end, direction, dictionary):
    danger_count = 0
    starting_point = min(start[direction], end[direction])
    ending_point = max(start[direction], end[direction])
    constant = start[1 - direction]
    for i in range(starting_point, ending_point+1, 1):
        coord = [0,0]
        coord[direction] = i
        coord[1 - direction] = constant
        coord = ",".join(str(item) for item in coord)
        if coord in dictionary.keys():
            if dictionary[coord] == 1:
                danger_count += 1
            dictionary[coord] += 1
        else:
            dictionary[coord] = 1
    return danger_count


if __name__ == "__main__":
    main()