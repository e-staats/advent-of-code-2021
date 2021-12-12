from rich import print


def main():
    pairing = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    scoring = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    score = 0
    with open("../inputs/day10.txt") as file:
        reading = True
        while reading == True:
            line = file.readline().rstrip()
            if line == "":
                reading = False
                continue
            score += score_line(line, pairing, scoring)
    print(score)


def score_line(line, pairing, scoring):
    stack = []
    for char in list(line):
        if char in pairing.keys():
            stack.append(char)
        else:
            opener = stack.pop()
            if char != pairing[opener]:
                return scoring[char]
    return 0


if __name__ == "__main__":
    main()
