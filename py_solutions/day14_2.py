from rich import print
from copy import deepcopy
from timer import timeit
from collections import Counter


@timeit
def main():
    instructions = {}
    with open("../inputs/day14.txt") as file:
        starter = file.readline().strip()
        chain_dict = parse_starter_to_dict(starter)
        file.readline()
        reading = True
        while reading == True:
            line = file.readline().strip()
            if line == "":
                reading = False
                continue
            pieces = line.split(" ")
            instructions[pieces[0]] = pieces[2]

    for step in range(40):
        chain_dict = polymer_chain_step(chain_dict, instructions)

    letter_count = analyze_chain(chain_dict, starter)
    ranked_letters = letter_count.most_common()
    print(ranked_letters)
    print(ranked_letters[0][1] - ranked_letters[-1][1])


def parse_starter_to_dict(starter):
    return_dict = {}
    for i in range(len(starter) - 1):
        pair = str(starter[i : i + 2])
        add_to_dict(return_dict, pair)
    return return_dict


def add_to_dict(dictionary, key, increment=1):
    if key in dictionary.keys():
        dictionary[key] += increment
    else:
        dictionary[key] = increment
    return


def polymer_chain_step(starter_dict, instructions):
    return_dict = {}
    for pair in starter_dict.keys():
        middle_letter = instructions[pair]
        add_to_dict(return_dict, pair[0] + middle_letter, starter_dict[pair])
        add_to_dict(return_dict, middle_letter + pair[1], starter_dict[pair])
    return return_dict


def analyze_chain(chain_dict, starter):
    letter_count = Counter()
    for pair in chain_dict.keys():
        letter_count.update({pair[0]: chain_dict[pair]})
        letter_count.update({pair[1]: chain_dict[pair]})
    # the start and end letters don't change but appear 1 less time than the
    # rest, which all get double counted by this method. So we add 1 to make it
    # even when we divide by 2 later
    letter_count.update(starter[0])
    letter_count.update(starter[-1])
    for item, count in letter_count.items():
        letter_count[item] = count // 2
    return letter_count


if __name__ == "__main__":
    main()
