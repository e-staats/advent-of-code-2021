from rich import print
from copy import deepcopy
import matplotlib.pyplot as plt
import time


def main():
    startTime = time.time()

    coordinate_dict = {}
    instructions = []
    with open("../inputs/day13.txt") as file:
        reading = True
        while reading == True:
            line = file.readline()
            if line == "":
                reading = False
                continue
            if line == "\n":
                while reading == True:
                    line = file.readline()
                    instruction = line.strip().split(" ")
                    if line == "":
                        reading = False
                        continue
                    instruction = instruction[2].split("=")
                    if instruction[0] == "x":
                        instruction[0] = 0
                    else:
                        instruction[0] = 1
                    instruction[1] = int(instruction[1])
                    instructions.append(instruction)
                continue
            coords = line.strip().split(",")
            coordinate_dict[get_location(coords[0], coords[1])] = [
                int(i) for i in coords
            ]

    instr = instructions[0]
    coordinate_dict = fold(coordinate_dict, instr[0], instr[1])
    print(len(coordinate_dict.keys()))

    executionTime = time.time() - startTime
    print("Execution time in seconds: " + str(executionTime))


def fold(coordinate_dict, axis, location):
    new_coordinate_dict = {}
    for str, coord in coordinate_dict.items():
        if coord[axis] > location:
            new_coord = deepcopy(coord)
            new_value = 2 * location - coord[axis]
            new_coord[axis] = new_value
            new_location = get_location(new_coord[0], new_coord[1])
            new_coordinate_dict[new_location] = new_coord
        else:
            new_coordinate_dict[str] = coord
    return new_coordinate_dict


def get_location(x, y):
    return "(" + str(x) + "," + str(y) + ")"


if __name__ == "__main__":
    main()
