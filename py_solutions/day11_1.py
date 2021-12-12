from rich import print


class Octopus:
    def __init__(self, energy=0, neighbors=[], flashed=False):
        self.energy = energy
        self.neighbors = neighbors
        self.flashed = flashed

    def increase_energy(self):
        self.energy += 1

    def attempt_flash(self, counter):
        if self.flashed == True:
            return counter
        if self.energy > 9:
            self.flashed = True
            counter += 1
            for neighbor in self.neighbors:
                neighbor.increase_energy()
                counter = neighbor.attempt_flash(counter)
        return counter

    def end_step(self):
        if self.flashed == True:
            self.energy = 0
            self.flashed = False


def main():
    with open("../inputs/day11.txt") as file:
        matrix = file.readlines()
        matrix = [row.strip() for row in matrix]

    mapped_octopi = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            location = get_location(i, j)
            if location not in mapped_octopi.keys():
                mapped_octopi[location] = Octopus(int(matrix[i][j]), [])
                mapped_octopi[location].neighbors = update_neighbors(
                    matrix, i, j, mapped_octopi
                )
            elif len(mapped_octopi[location].neighbors) == 0:
                mapped_octopi[location].neighbors = update_neighbors(
                    matrix, i, j, mapped_octopi
                )

    count = 0
    for step in range(100):
        for loc in mapped_octopi.keys():
            mapped_octopi[loc].increase_energy()

        for loc in mapped_octopi.keys():
            count = mapped_octopi[loc].attempt_flash(count)

        for loc in mapped_octopi.keys():
            mapped_octopi[loc].end_step()

    print(count)


def get_neighbors(matrix, x, y):
    locations = []
    ranges = [[0, 0], [0, 0]]
    if x - 1 >= 0:
        ranges[0][0] = -1
    if x + 1 < len(matrix[0]):
        ranges[0][1] = 1
    if y - 1 >= 0:
        ranges[1][0] = -1
    if y + 1 < len(matrix):
        ranges[1][1] = 1
    for i in range(ranges[0][0], ranges[0][1] + 1):
        for j in range(ranges[1][0], ranges[1][1] + 1):
            if i == 0 and j == 0:
                continue
            locations.append(get_location(x + i, y + j))
    return locations


def update_neighbors(matrix, i, j, mapped_octopi):
    neighbors = []
    neighboring_locations = get_neighbors(matrix, i, j)
    for l in neighboring_locations:
        if l in mapped_octopi.keys():
            neighbors.append(mapped_octopi[l])
        else:
            temp_loc = l.strip("()").split(",")
            temp_octo = Octopus(int(matrix[int(temp_loc[0])][int(temp_loc[1])]), [])
            neighbors.append(temp_octo)
            mapped_octopi[l] = temp_octo
    return neighbors


def get_location(x, y):
    return "(" + str(x) + "," + str(y) + ")"


if __name__ == "__main__":
    main()
