from rich import print


def main():
    pairing = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    scoring = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    score = []
    with open("../inputs/day10.txt") as file:
        reading = True
        while reading == True:
            line = file.readline().rstrip()
            if line == "":
                reading = False
                continue
            line_score = score_line(line, pairing, scoring)
            if line_score > 0:
                score.append(line_score)
    score.sort()
    print(score)
    print(score[len(score)//2])


def score_line(line, pairing, scoring):
    stack = []
    score = 0
    for char in list(line):
        if char in pairing.keys():
            stack.append(char)
        else:
            opener = stack.pop()
            if char != pairing[opener]:
                return 0
    while len(stack) > 0:
        opener = stack.pop()
        closer = pairing[opener]
        score = (score * 5) + scoring[closer]
    return score


if __name__ == "__main__":
    main()
