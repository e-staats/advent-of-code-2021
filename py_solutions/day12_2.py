from rich import print
from copy import deepcopy
import time


class CaveSystem:
    def __init__(self, caves=[]):
        self.caves = caves
        self.path_count = 0

    def cave_exist(self, cave_name):
        for cave in self.caves:
            if cave.name == cave_name:
                return True
        return False

    def get_cave(self, cave_name):
        for cave in self.caves:
            if cave.name == cave_name:
                return cave
        return False

    def add_cave(self, cave):
        self.caves.append(cave)

    def list_caves(self):
        for cave in self.caves:
            print(cave.name, end=" ")
            print([c.name for c in cave.edges])

    def search(self, current_cave, visited, path, one_time_minor_cave):
        # print(f"at {current_cave.name}, having visited {visited} and current path is {path}")
        if current_cave.name == "end":
            # print(path)
            self.path_count += 1
            return
        for cave in current_cave.edges:
            new_visited = deepcopy(visited)
            new_path = deepcopy(path)
            new_one_time_minor_cave = deepcopy(one_time_minor_cave)
            if (
                cave.type == "minor"
                and cave.name != "start"
                and cave.name != "end"
                and cave.name in visited
                and one_time_minor_cave == None
            ):
                new_path.append(cave.name)
                new_visited.add(cave.name)
                new_one_time_minor_cave = cave.name
                self.search(cave, new_visited, new_path, new_one_time_minor_cave)
            elif cave.type == "minor" and cave.name not in visited:
                new_path.append(cave.name)
                new_visited.add(cave.name)
                self.search(cave, new_visited, new_path, new_one_time_minor_cave)
            elif cave.type == "major":
                new_path.append(cave.name)
                new_visited.add(cave.name)
                self.search(cave, new_visited, new_path, new_one_time_minor_cave)


class Cave:
    def __init__(self, name):
        self.name = name
        if name.isupper() == True:
            self.type = "major"
        else:
            self.type = "minor"
        self.edges = []

    def add_edge(self, destination):
        # print(f"adding {destination.name} to {self.name}")
        self.edges.append(destination)


def main():
    startTime = time.time()
    with open("../inputs/day12.txt") as file:
        rows = file.readlines()
        rows = [row.strip().split("-") for row in rows]

    caves = CaveSystem()

    for row in rows:
        if caves.cave_exist(row[0]) == False:
            cave1 = Cave(row[0])
            caves.add_cave(cave1)
        else:
            cave1 = caves.get_cave(row[0])
        if caves.cave_exist(row[1]) == False:
            cave2 = Cave(row[1])
            caves.add_cave(cave2)
        else:
            cave2 = caves.get_cave(row[1])

        cave1.add_edge(cave2)
        cave2.add_edge(cave1)

    start = caves.get_cave("start")
    visited = {"start"}
    path = ["start"]
    caves.search(start, visited, path, None)
    print(caves.path_count)

    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))



if __name__ == "__main__":
    main()
