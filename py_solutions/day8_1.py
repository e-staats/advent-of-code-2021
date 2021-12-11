from rich import print

def main():
    inputs = []
    outputs = []
    with open("../inputs/day8.txt") as file:
        reading = True
        while reading == True:
            line = file.readline()
            if line == "":
                reading = False
                continue
            line = line.rstrip().split("|")
            inputs.append(line[0])
            outputs += [x for x in line[1].strip().split(" ")]
    count = 0
    for item in outputs:
        length = len(item)
        if length == 2 or length == 4 or length == 3 or length == 7:
            count += 1
        else:
            print(item)
    print(len(outputs))
    print(count)

if __name__ == "__main__":
    main()
