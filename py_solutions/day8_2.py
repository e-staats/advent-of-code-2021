from rich import print


def main():
    inputs = []
    outputs = []
    data = []
    with open("../inputs/day8.txt") as file:
        reading = True
        while reading == True:
            line = file.readline()
            if line == "":
                reading = False
                continue
            line = line.rstrip().split("|")
            data.append(
                [
                    [x for x in line[0].strip().split(" ")],
                    [y for y in line[1].strip().split(" ")],
                ]
            )
    count = 0
    for line in data:
        starter = {
            5: [],
            6: [],
        }
        decode = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 0: ""}
        mapping = {'a': '','b': '','c': '','d': '','e': '','f': '','g': ''}
        for input in line[0]:
            length = len(input)
            if length == 2:
                decode[1] = set(input)
            elif length == 4:
                decode[4] = set(input)
            elif length == 3:
                decode[7] = set(input)
            elif length == 7:
                decode[8] = set(input)
            else:
                starter[length].append(set(input))
        mapping['a'] = (decode[7] - decode[1]).pop()
        find_g(starter, decode, mapping)
        print(mapping)

def find_g(starter, decode, mapping):
    print(decode[4])
    print(mapping['a'])
    decode[4].add(mapping['a'])
    print(check)
    for set in starter:
        diff = check - set
        if len(diff) == 1:
            mapping['g'] = diff.pop()
            return

if __name__ == "__main__":
    main()
